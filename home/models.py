from typing import ClassVar

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from home.blocks import (
    AboutBlock,
    BlogFeedBlock,
    ClientsBlock,
    HomeBlock,
    HomeContactBlock,
    ServicesBlock,
    TestimoniesBlock,
)


@register_setting
class ConfiguracionSitio(BaseSiteSetting):
    nombre_sitio = models.CharField(max_length=100, verbose_name="Nombre del sitio")
    sufijo_titulo = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Eslogan",
    )
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Logo principal",
    )

    panels: ClassVar[tuple[FieldPanel, ...]] = (
        MultiFieldPanel(
            [
                FieldPanel("nombre_sitio"),
                FieldPanel("sufijo_titulo"),
                FieldPanel("logo"),
            ],
            heading="Branding General",
        ),
    )

    class Meta:
        verbose_name = "Configuración Global"


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    x = models.URLField(
        blank=True,
        verbose_name="X (Twitter)",
    )
    facebook = models.URLField(
        blank=True,
        verbose_name="Facebook",
    )
    instagram = models.URLField(
        blank=True,
        verbose_name="Instagram",
    )
    youtube = models.URLField(
        blank=True,
        verbose_name="YouTube",
    )
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")

    panels: ClassVar[tuple[FieldPanel, ...]] = (
        MultiFieldPanel(
            [
                FieldPanel("x"),
                FieldPanel("facebook"),
                FieldPanel("instagram"),
                FieldPanel("youtube"),
                FieldPanel("linkedin"),
            ],
            heading="Redes Sociales",
        ),
    )

    class Meta:
        verbose_name = "Redes Sociales"


class StandardPage(Page):
    subtitular = models.CharField(max_length=255, blank=True, verbose_name="Subtítulo")
    cuerpo = RichTextField(verbose_name="Contenido legal")

    content_panels = Page.content_panels + [
        FieldPanel("subtitular"),
        FieldPanel("cuerpo"),
    ]

    parent_page_types: ClassVar[tuple[str, ...]] = ("home.HomePage",)


class ContactFormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class ContactPage(AbstractEmailForm):
    subtitular = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Subtítulo",
        help_text="Ej: 'Conversemos sobre cómo potenciar la comunicación de tu empresa.'",
    )
    intro = RichTextField(
        blank=True, verbose_name="Texto introductorio / Información de contacto"
    )
    mensaje_agradecimiento = RichTextField(
        blank=True,
        verbose_name="Mensaje de éxito",
        help_text="Mensaje que verá el usuario tras enviar el formulario.",
    )

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("subtitular"),
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Campos del formulario"),
        FieldPanel("mensaje_agradecimiento"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            heading="Configuración de correo (Notificaciones)",
        ),
    ]

    parent_page_types: ClassVar[tuple[str, ...]] = ("home.HomePage",)


class HomePage(Page):
    cuerpo = StreamField(
        [
            ("hero", HomeBlock()),
            ("about", AboutBlock()),
            ("servicios", ServicesBlock()),
            ("clientes", ClientsBlock()),
            ("testimonios", TestimoniesBlock()),
            ("blog_feed", BlogFeedBlock()),
            ("contacto", HomeContactBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("cuerpo"),
    ]
