import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))

@register.simple_tag()
def avatar(uid):
    tag = f'<img class="avatar" src="https://randomuser.me/api/portraits/men/{uid}.jpg"/>'
    return mark_safe(tag)

@register.simple_tag()
def has_vote(obj, user):
    if obj.voter.contains(user) :
        tag = '<i class="fa-solid fa-heart text-danger"></i>'
    else:
        tag = '<i class="fa-regular fa-heart  text-danger"></i>'
    return mark_safe(tag)




# {% avatar user.id %}