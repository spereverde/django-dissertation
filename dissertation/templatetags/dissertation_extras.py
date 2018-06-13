import requests

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def include_external(url):
    include = requests.get(url)
    include_safe = mark_safe(include.text)
    return include_safe