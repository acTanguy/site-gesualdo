from django import template

register = template.Library()

@register.filter(name="coupeUrl")
def coupeUrl(value, width):
	return value[:-width]