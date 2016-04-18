from django import template

register = template.Library()


@register.inclusion_tag('_included.html')
def inclusion_tagged(number, level, depth):
    return {
        'number': number,
        'depth': depth,
        'level': level + 1,
    }
