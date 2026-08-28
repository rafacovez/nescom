from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class NewsletterSubscriber(models.Model):
    email = models.EmailField(
        unique=True, max_length=255, verbose_name="Correo electrónico"
    )
    nombre = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Nombre"
    )
    origen = models.CharField(
        max_length=100, default="Formulario de contacto", verbose_name="Origen"
    )
    activo = models.BooleanField(default=True, verbose_name="Activo")
    creado_en = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de suscripción"
    )

    panels = (
        FieldPanel("email"),
        FieldPanel("nombre"),
        FieldPanel("origen"),
        FieldPanel("activo"),
    )

    class Meta:
        verbose_name = "Suscriptor de Newsletter"
        verbose_name_plural = "Suscriptores de Newsletter"
        ordering = ("-creado_en",)

    def __str__(self):
        return self.email
