from django import template
from datetime import datetime
from django.utils.timezone import localtime

register = template.Library()

@register.filter
def data_format_y_m_d(value):
    if not isinstance(value, datetime):
        return value
    return localtime(value).strftime("%Y-%m-%d")
