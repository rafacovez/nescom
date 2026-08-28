from wagtail import blocks


class BaseBlogFeedBlock(blocks.StructBlock):
    titular = blocks.CharBlock(
        required=True,
        max_length=100,
        default="Últimas Publicaciones",
        label="Título de la sección",
    )
    subtitular = blocks.TextBlock(
        required=False, rows=2, label="Subtítulo o descripción"
    )
    pagina_blog = blocks.PageChooserBlock(
        required=False,
        page_type=["blog.BlogIndexPage", "wagtailcore.Page"],
        label="Página del Blog",
        help_text="Selecciona la página principal del blog para el enlace 'Ver todos'.",
    )
    limite = blocks.IntegerBlock(
        default=3, min_value=1, max_value=6, label="Cantidad de artículos a mostrar"
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        blog_page = value.get("pagina_blog")
        limite = value.get("limite", 3)

        if blog_page:
            context["articulos"] = (
                blog_page.get_children()
                .live()
                .public()
                .order_by("-first_published_at")[:limite]
                .specific()
            )
        else:
            context["articulos"] = []
        return context
