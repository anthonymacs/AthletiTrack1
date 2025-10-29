# core/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Allows you to get an item from a dictionary using a variable key in a template.
    Usage: {{ my_dictionary|get_item:my_variable }}
    """
    return dictionary.get(key)