from django import template

register = template.Library()


@register.filter()
def ranges(abc):
    return abc[0]


@register.filter()
def rangess(abc):
    return abc[1]
