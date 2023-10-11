from django import template

from apps.models import Brand

register = template.Library()


@register.simple_tag
def get_all_brands():
    return Brand.objects.all()