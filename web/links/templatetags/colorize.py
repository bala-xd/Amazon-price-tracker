from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def colorize(val):
    mark = str(val)[:1]
    if mark == "-":
        html_string = f"<span style='color:green; font-weight:bold;'>{val}</span>"
    elif mark == "0":
        html_string = f"<span style='color:blue; font-weight:bold;'>{val}</span>"
    else:
        html_string = f"<span style='color:red; font-weight:bold;'>{val}</span>"
    return mark_safe(html_string)