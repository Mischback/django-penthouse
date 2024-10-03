# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific exceptions."""


class PenthouseException(Exception):
    """Base class for all app-specific exceptions."""


class PenthouseModelException(PenthouseException):
    """Base class for all app-specific and model-related exceptions."""
