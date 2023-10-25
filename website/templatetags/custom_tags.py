from django import template

register = template.Library()

@register.filter
def truncate_to_ten_words(value):
    words = value.split()
    if len(words) > 10:
        return ' '.join(words[:10]) + '...'
    else:
        return value
