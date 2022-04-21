from django import template
import pathlib

register = template.Library()

# Getting file name only or None
def file_name(value):
    try:
        path = pathlib.Path(value)

        return path.name
    except ValueError:
        return None

register.filter('file_name', file_name)