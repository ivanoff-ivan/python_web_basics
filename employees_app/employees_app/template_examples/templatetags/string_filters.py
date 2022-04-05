from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize_filter(value):
    """
    * THis is TeXt => This is text
    """
    value = str(value)
    return value[0].upper() + value[1:].lower()



