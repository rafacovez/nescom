from django import template

from blog.models import BlogCategory, BlogIndexPage, BlogPostPage
from home.models import ContactPage, StandardPage

register = template.Library()


def _categories_for_blog(index_page):
    index_page = index_page.specific
    allowed = index_page.allowed_categories.all()
    if allowed.exists():
        return list(allowed.order_by("nombre"))
    return list(
        BlogCategory.objects.filter(
            posts__in=BlogPostPage.objects.descendant_of(index_page).live()
        )
        .distinct()
        .order_by("nombre")
    )


@register.simple_tag
def categories_for_blog(index_page):
    return _categories_for_blog(index_page)


@register.simple_tag
def get_site_navigation():
    contact_page = ContactPage.objects.live().public().first()

    blogs = list(BlogIndexPage.objects.live().public())
    for blog in blogs:
        blog.nav_categories = _categories_for_blog(blog)

    return {
        "blogs": blogs,
        "legal_pages": StandardPage.objects.live().public().order_by("title"),
        "contact_page": contact_page,
    }
