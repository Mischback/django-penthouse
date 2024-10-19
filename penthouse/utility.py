"""App-specific utility functions."""

# app imports
from penthouse.game_constants import TowerUnits


def seconds_to_hms(value):
    """Convert seconds to dedicated hour, minute and second components."""
    # I fucking love Python!
    # https://stackoverflow.com/a/775075
    m, s = divmod(value, 60)
    h, m = divmod(m, 60)

    return h, m, s


def get_number_prefix(value):
    """Provide a short notation for big numbers."""
    for prefix, mult in TowerUnits.get_multiplier_prefix().items():
        # print("{}-{}".format(prefix, mult))
        numerical = value / (10**mult)
        if numerical >= 1:
            return numerical, prefix

    return value, ""
