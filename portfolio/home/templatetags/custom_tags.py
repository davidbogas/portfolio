from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def svg(file_field):
    try:
        with open(file_field.path, 'r', encoding='utf-8') as svg_file:
            return mark_safe(svg_file.read())
    except (FileNotFoundError, IOError):
        return ''