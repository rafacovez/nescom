import time
from typing import ClassVar

from django.core.cache import cache
from django.core.mail import send_mail
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
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
from home.forms import ContactForm


@register_setting
class ConfiguracionSitio(BaseSiteSetting):
    nombre_sitio = models.CharField(max_length=100, verbose_name="Nombre del sitio")
    blog_share_cta_text = models.CharField(
        max_length=100,
        blank=True,
        default="Compártelo",
        verbose_name="Texto de llamada a la acción para compartir posts",
        help_text="Aparecerá en los botones de compartir de todos los artículos del blog.",
    )
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
                FieldPanel("blog_share_cta_text"),
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


class ContactPage(Page):
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
    to_address = models.EmailField(
        blank=True,
        verbose_name="Correo de destino",
        help_text="A dónde llegarán las notificaciones de contacto.",
    )
    subject = models.CharField(
        max_length=255,
        blank=True,
        default="Nuevo mensaje de contacto desde el sitio web",
        verbose_name="Asunto del correo",
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitular"),
        FieldPanel("intro"),
        FieldPanel("mensaje_agradecimiento"),
        MultiFieldPanel(
            [
                FieldPanel("to_address"),
                FieldPanel("subject"),
            ],
            heading="Configuración de correo (Notificaciones)",
        ),
    ]

    parent_page_types: ClassVar[tuple[str, ...]] = ("home.HomePage",)

    def get_context(self, request):
        context = super().get_context(request)

        if request.method == "POST":
            form = ContactForm(request.POST)

            is_spam = False

            if form.is_valid() and form.cleaned_data.get("hp_website"):
                is_spam = True

            if form.is_valid():
                try:
                    token_time = float(form.cleaned_data.get("form_timestamp", 0))
                    if time.time() - token_time < 3.0:
                        is_spam = True
                except (ValueError, TypeError):
                    is_spam = True

            client_ip = request.META.get("REMOTE_ADDR")
            rate_limit_key = f"contact_rate_{client_ip}"
            if cache.get(rate_limit_key):
                is_spam = True
            else:
                cache.set(rate_limit_key, True, timeout=600)

            if form.is_valid() and not is_spam:
                data = form.cleaned_data

                if self.to_address:
                    email_body = f"Nombre: {data['nombre']}\nCorreo: {data['email']}\n\nMensaje:\n{data['mensaje']}"
                    send_mail(
                        self.subject,
                        email_body,
                        None,
                        [self.to_address],
                        fail_silently=False,
                    )

                if data.get("newsletter_opt_in"):
                    from newsletter.models import (
                        NewsletterSubscriber,
                    )

                    NewsletterSubscriber.objects.get_or_create(
                        email=data["email"], defaults={"nombre": data["nombre"]}
                    )

                context["submitted"] = True
                context["form"] = ContactForm(initial={"form_timestamp": time.time()})
            else:
                context["form"] = form
        else:
            context["form"] = ContactForm(initial={"form_timestamp": time.time()})
            context["submitted"] = False

        return context


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
