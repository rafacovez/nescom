from typing import ClassVar

from django import forms
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase
from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page
from wagtail.snippets.models import register_snippet


@register_snippet
class Author(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="author_profiles",
        verbose_name="Usuario del sistema",
        help_text="Selecciona el usuario del sistema al que pertenece este perfil.",
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    cargo = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="Cargo / Rol",
        help_text="Ej: 'Consultor de Comunicación' o 'Director General'",
    )
    foto = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Foto de perfil",
    )

    panels: ClassVar[tuple[FieldPanel, ...]] = (
        FieldPanel("nombre"),
        FieldPanel("cargo"),
        FieldPanel("foto"),
        FieldPanel("user"),
    )

    @property
    def inicial(self) -> str:
        return self.nombre.strip()[0].upper() if self.nombre.strip() else "?"

    def __str__(self):
        return f"{self.nombre} ({self.cargo})" if self.cargo else self.nombre

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


@register_snippet
class BlogCategory(models.Model):
    nombre = models.CharField(max_length=60, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    panels: ClassVar[tuple[FieldPanel, ...]] = (FieldPanel("nombre"),)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Blog"
        verbose_name_plural = "Categorías de Blog"


class BlogPostTag(TaggedItemBase):
    content_object = ParentalKey(
        "blog.BlogPostPage",
        on_delete=models.CASCADE,
        related_name="tagged_items",
    )


class BlogPostFuente(Orderable):
    page = ParentalKey(
        "blog.BlogPostPage",
        on_delete=models.CASCADE,
        related_name="fuentes",
    )
    nombre = models.CharField(
        max_length=120,
        verbose_name="Nombre de la fuente / medio",
        help_text="Ej: 'The New York Times', 'Banco Central', 'Reuters'",
    )
    enlace = models.URLField(
        blank=True,
        verbose_name="Enlace a la fuente (opcional)",
    )
    foto = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Logo o imagen de la fuente (opcional)",
    )

    panels: ClassVar[tuple[FieldPanel, ...]] = (
        FieldPanel("nombre"),
        FieldPanel("enlace"),
        FieldPanel("foto"),
    )

    @property
    def inicial(self) -> str:
        return self.nombre.strip()[0].upper() if self.nombre.strip() else "?"


class BlogIndexPage(Page):
    intro = RichTextField(blank=True, help_text="Descripción o introducción del blog")
    allowed_categories = ParentalManyToManyField(
        "blog.BlogCategory",
        blank=True,
        related_name="allowed_in_blogs",
        verbose_name="Categorías permitidas",
        help_text="Deja vacío para permitir todas las categorías en este blog.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("allowed_categories", widget=forms.CheckboxSelectMultiple),
    ]

    subpage_types: ClassVar[tuple[str, ...]] = ("blog.BlogPostPage",)

    def get_context(self, request):
        context = super().get_context(request)
        posts = (
            BlogPostPage.objects.child_of(self)
            .live()
            .public()
            .order_by("-fecha_publicacion")
        )
        tag = request.GET.get("tag")
        if tag:
            posts = posts.filter(tags__slug=tag)
        categoria = request.GET.get("categoria")
        if categoria:
            posts = posts.filter(categorias__slug=categoria).distinct()

        context["posts"] = posts
        context["selected_tag"] = tag
        context["selected_categoria"] = categoria
        return context


class BlogPostPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parent = self.parent_page or (
            self.instance.get_parent() if self.instance.pk else None
        )
        if parent:
            allowed = parent.specific.allowed_categories.all()
            if allowed.exists():
                self.fields["categorias"].queryset = allowed


class BlogPostPage(Page):
    fecha_publicacion = models.DateTimeField(
        default=timezone.now,
        blank=True,
        verbose_name="Fecha de publicación",
        help_text="Si se deja en blanco, tomará la fecha y hora actual automáticamente.",
    )
    portada = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Foto de portada",
    )
    autores = ParentalManyToManyField(
        "blog.Author",
        blank=False,
        related_name="posts",
        verbose_name="Autores",
        help_text="Selecciona al menos un autor para este artículo.",
    )
    categorias = ParentalManyToManyField(
        "blog.BlogCategory",
        blank=False,
        related_name="posts",
        verbose_name="Categorías",
        help_text="Selecciona al menos una categoría para este artículo.",
    )
    tags = ClusterTaggableManager(
        through=BlogPostTag, blank=True, verbose_name="Etiquetas (Tags)"
    )
    cuerpo = RichTextField("Contenido del artículo")

    base_form_class = BlogPostPageForm

    content_panels = Page.content_panels + [
        FieldPanel("fecha_publicacion"),
        FieldPanel("portada"),
        FieldPanel("autores", widget=forms.CheckboxSelectMultiple),
        MultiFieldPanel(
            (
                FieldPanel("categorias", widget=forms.CheckboxSelectMultiple),
                FieldPanel("tags"),
            ),
            heading="Clasificación",
        ),
        FieldPanel("cuerpo"),
        InlinePanel(
            "fuentes",
            max_num=5,
            label="Fuente de información",
            heading="Fuentes consultadas (máx. 5)",
        ),
    ]

    parent_page_types: ClassVar[tuple[str, ...]] = ("blog.BlogIndexPage",)

    def save(self, *args, **kwargs):
        if not self.fecha_publicacion:
            self.fecha_publicacion = timezone.now()
        super().save(*args, **kwargs)
