from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import linebreaks

register = template.Library()

@register.filter
def safe_linebreaks(value):
    """
        Marks the value as a safe string and then converts newlines into <p> and <br> tags.
    """
    return linebreaks(mark_safe(value))