"""Implementation of the app-specific templatetags."""

# Django imports
from django.template import Library

# app imports
from penthouse.utility import get_number_prefix, seconds_to_hms

# create a valid Django templatetag library
register = Library()


@register.filter
def hr_duration(value):
    """Convert a duration given in seconds to human-readable format (h m s)."""
    h, m, s = seconds_to_hms(value)

    return "{}h {}m {}s".format(h, m, s)


@register.filter
def hr_big_number(value):
    """Provide number notation with prefix."""
    numerical, prefix = get_number_prefix(value)

    return "{:0.2f}{}".format(numerical, prefix)
