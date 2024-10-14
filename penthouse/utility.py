"""App-specific utility functions."""


def seconds_to_hms(value):
    """Convert seconds to dedicated hour, minute and second components."""
    # I fucking love Python!
    # https://stackoverflow.com/a/775075
    m, s = divmod(value, 60)
    h, m = divmod(m, 60)

    return h, m, s
