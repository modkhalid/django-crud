from django import template

register=template.Library()

@register.filter(name="cut")
def cut(st,arg):
    return str(st).replace(arg,'')
    