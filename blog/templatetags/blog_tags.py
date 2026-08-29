from django import template

from blog.models import BlogCategory, BlogIndexPage
from home.models import StandardPage

register = template.Library()


@register.simple_tag
def get_site_navigation():
    contact_page = (
        StandardPage.objects.live()
        .public()
        .filter(slug__in=["contacto", "contact", "contact-us"])
        .first()
    )

    return {
        "blogs": BlogIndexPage.objects.live().public(),
        "categories": BlogCategory.objects.all().order_by("nombre"),
        "legal_pages": StandardPage.objects.live().public().order_by("title"),
        "contact_page": contact_page,
    }
