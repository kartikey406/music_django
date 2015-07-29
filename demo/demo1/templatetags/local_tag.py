from django import template
register = template.Library()
value={}
@register.filter(name='get_key')
def get_key(value):
    return value['#text']
