# Code Institute
from django import template

register = template.Library()


# ChatGPT Code
@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    try:
        return float(price) * int(quantity)
    except (TypeError, ValueError):
        return 0
