from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class LinkChoiceBlock(blocks.StreamBlock):
    pagina = blocks.PageChooserBlock(
        label="Página interna",
        help_text="Selecciona una página existente de tu sitio web.",
    )
    url_externa = blocks.URLBlock(
        label="Enlace externo",
        help_text="O escribe una URL completa (ej. https://ejemplo.com).",
    )

    class Meta:
        max_num = 1
        min_num = 1
        label = "Enlace de destino"


class CTAButtonBlock(blocks.StructBlock):
    texto = blocks.CharBlock(
        required=True, max_length=50, label="Texto del botón", default="Texto"
    )
    enlace = LinkChoiceBlock()

    class Meta:
        template = "blocks/cta_block.html"
        icon = "link"
        label = "Botón de acción"


class HomeBlock(blocks.StructBlock):
    portada = ImageChooserBlock(
        required=False,
        help_text="Imagen de portada del bloque de inicio.",
    )
    credito_imagen = blocks.CharBlock(
        required=False,
        max_length=100,
        help_text="Discreto en la esquina inferior (opcional). Ej: 'Foto por Unsplash'",
    )
    enlace_credito = blocks.URLBlock(
        required=False, help_text="Enlace al portfolio del autor (opcional)."
    )
    titular = blocks.CharBlock(
        required=True, max_length=150, help_text="Titular del bloque de inicio."
    )
    subtitular = blocks.CharBlock(
        required=False, max_length=250, help_text="Subtitular del bloque de inicio."
    )
    boton = CTAButtonBlock(required=False, help_text="Botón del bloque de inicio.")

    class Meta:
        template = "blocks/home_block.html"
        icon = "image"
        label = "Sección de inicio"


class ValorItemBlock(blocks.StructBlock):
    titulo = blocks.CharBlock(required=True, max_length=60, label="Nombre del valor")

    class Meta:
        icon = "tick"
        label = "Valor corporativo"


class AboutBlock(blocks.StructBlock):
    titular = blocks.CharBlock(
        required=True,
        max_length=100,
        default="Sobre nosotros",
        label="Título de la sección",
    )
    subtitular = blocks.TextBlock(
        required=False, rows=2, label="Subtítulo o descripción introductoria"
    )
    logo = ImageChooserBlock(required=False, label="Foto de la empresa / equipo")
    mision = blocks.TextBlock(required=True, rows=4, label="Misión")
    vision = blocks.TextBlock(required=True, rows=4, label="Visión")
    valores = blocks.ListBlock(
        ValorItemBlock(), label="Valores corporativos", min_num=1
    )

    class Meta:
        template = "blocks/about_block.html"
        icon = "group"
        label = "Sección de sobre nosotros (Misión, Visión, Valores)"


class ServiceItemBlock(blocks.StructBlock):
    imagen = ImageChooserBlock(
        required=True,
        label="Foto del servicio",
        help_text="Proporción recomendada vertical o 4:5",
    )
    titulo = blocks.CharBlock(required=True, max_length=60, label="Título del servicio")
    descripcion = blocks.TextBlock(
        required=True, max_length=200, rows=3, label="Descripción breve"
    )
    pagina = blocks.PageChooserBlock(
        label="Página interna",
        help_text="Selecciona una página existente de tu sitio web.",
    )

    class Meta:
        icon = "doc-full"
        label = "Servicio"


class ServicesBlock(blocks.StructBlock):
    titular = blocks.CharBlock(
        required=True,
        max_length=100,
        default="Nuestros servicios",
        label="Título de la sección",
    )
    subtitular = blocks.TextBlock(
        required=False, rows=2, label="Subtítulo o descripción"
    )
    servicios = blocks.ListBlock(
        ServiceItemBlock(), min_num=4, max_num=12, label="Lista de servicios"
    )

    class Meta:
        template = "blocks/services_block.html"
        icon = "list-ul"
        label = "Sección de servicios"


class ClientItemBlock(blocks.StructBlock):
    logo = ImageChooserBlock(
        required=True,
        label="Logo de la empresa",
        help_text="Logo rectangular con fondo transparente (PNG, SVG o WebP).",
    )
    enlace_externo = blocks.URLBlock(
        required=True,
        label="Sitio web del cliente",
        help_text="Ejemplo: https://cliente.com",
    )

    class Meta:
        icon = "image"
        label = "Cliente / Empresa"


class ClientsBlock(blocks.StructBlock):
    titular = blocks.CharBlock(
        required=True,
        max_length=100,
        default="Nuestros clientes",
        label="Título de la sección",
    )
    subtitular = blocks.TextBlock(
        required=False,
        rows=2,
        label="Subtítulo (opcional)",
    )
    clientes = blocks.ListBlock(
        ClientItemBlock(), min_num=1, max_num=20, label="Lista de clientes"
    )

    class Meta:
        template = "blocks/clients_block.html"
        icon = "group"
        label = "Sección de clientes"


class TestimonyItemBlock(blocks.StructBlock):
    foto_perfil = ImageChooserBlock(
        required=True,
        label="Foto de perfil",
        help_text="Retrato de la persona (proporción cuadrada recomendada).",
    )
    testimonio = blocks.TextBlock(
        required=True,
        rows=4,
        label="Testimonio / Palabras",
        help_text="Las palabras o reseña compartida por la persona.",
    )
    nombre = blocks.CharBlock(required=True, max_length=80, label="Nombre completo")
    cargo = blocks.CharBlock(
        required=True,
        max_length=100,
        label="Cargo / Profesión / Rol",
        help_text="Ej: Directora Ejecutiva, Fundación Popular",
    )

    class Meta:
        icon = "user"
        label = "Testimonio"


class TestimoniesBlock(blocks.StructBlock):
    titular = blocks.CharBlock(
        required=True,
        max_length=100,
        default="Testimonios",
        label="Título de la sección",
    )
    subtitular = blocks.TextBlock(required=False, rows=2, label="Subtítulo (opcional)")
    testimonios = blocks.ListBlock(
        TestimonyItemBlock(), min_num=3, max_num=6, label="Lista de testimonios"
    )

    class Meta:
        template = "blocks/testimonies_block.html"
        icon = "openquote"
        label = "Sección de Testimonios"


class HomeContactBlock(blocks.StructBlock):
    etiqueta = blocks.CharBlock(default="Contacto", max_length=40, required=False)
    titular = blocks.CharBlock(
        default="Hablemos de tu próximo proyecto", max_length=120
    )
    subtitular = blocks.TextBlock(required=False)
    pagina_contacto = blocks.PageChooserBlock(
        page_type=["home.ContactPage"],
        label="Página de Contacto Destino",
    )

    class Meta:
        template = "blocks/home_contact_block.html"
        icon = "mail"
        label = "Sección: Formulario de Contacto"


class BlogFeedBlock(blocks.StructBlock):
    pagina_blog = blocks.PageChooserBlock(
        required=True,
        page_type=["blog.BlogIndexPage"],
        label="Seleccionar Blog",
        help_text="El título, introducción y artículos se mostrarán automáticamente desde esta página.",
    )
    limite = blocks.IntegerBlock(
        default=3,
        min_value=1,
        max_value=6,
        label="Cantidad de artículos",
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        blog_page = value.get("pagina_blog")
        limite = value.get("limite", 3)

        if blog_page:
            blog_page_specific = blog_page.specific
            context["blog_page"] = blog_page_specific
            context["articulos"] = (
                blog_page_specific.get_children()
                .live()
                .public()
                .order_by("-first_published_at")[:limite]
                .specific()
            )
        else:
            context["blog_page"] = None
            context["articulos"] = []
        return context

    class Meta:
        template = "blocks/blog_feed_block.html"
        icon = "doc-full-inverse"
        label = "Sección: Vista previa de Blog"
