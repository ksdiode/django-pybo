from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def avarta(context, id):
    tag = f'<img class="avarta" src="https://randomuser.me/api/portraits/men/{id}.jpg"/>'
    # 
    return mark_safe(tag)
