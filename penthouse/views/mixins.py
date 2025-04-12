# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific mixins to be used with class-based views."""

# Django imports
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.utils.translation import gettext_lazy as _


class ProvideActiveAccountMixin:
    """Provide the currently active account in the CBV and the rendering context.

    The currently active account is used in several places throughout the
    backend and frontend code. The actual implementation to get the account is
    highly dependent on the actual view, which will have to implement
    :meth:`~penthouse.views.mixins.ProvideActiveAccountMixin.get_active_account`
    for the dedicated situation, depending on the available parameters.

    The actual account is then available as ``self.active_account`` in the CBV
    and in the rendering context as ``active_account``.
    """

    def dispatch(self, request, *args, **kwargs):
        """Add the currently active account to the CBV instance."""
        self.active_account = self.get_active_account()

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        """Add the currently active account to the rendering context."""
        context = super().get_context_data(*args, **kwargs)

        context["active_account"] = self.active_account

        return context

    def get_active_account(self):
        """Retrieve the currently active account.

        This method is not implemented add requires to be implemented in the
        actual CBV, as it is dependent on the actual view how to get the
        currently active account.
        """
        raise NotImplementedError("Needs implementation in actual CBV")


class RestrictToUserMixin:
    """Limits the resulting queryset to objects, that belong to the current user.

    This mixin overwrites the view's ``get_queryset()`` method and automatically
    uses the model's app-specific ``ModelManager``.
    """

    def get_queryset(self):  # noqa: D102
        if self.model is None:
            raise ImproperlyConfigured(
                "{} is missing the 'model' attribute".format(self.__class__.__name__)
            )

        return self.model.objects.filter_by_user(user=self.request.user)

    def get_object(self, queryset=None):
        """Return the object to work on.

        Several of Django's generic views use the implementation of
        ``django.views.generic.detail.SingleObjectMixin`` to fetch the actual
        object. This method relies on URL parameters (pk or slug) to identify
        the object.

        For some of the app-specific models, this is not required, as there is
        a 1:1-relation to the project's ``AUTH_USER_MODEL``.
        """
        if queryset is None:
            queryset = self.get_queryset()

        try:
            return super().get_object(queryset=queryset)
        except AttributeError:
            try:
                obj = queryset.get()
            except queryset.model.DoesNotExist:
                raise Http404(
                    _("No %(verbose_name)s found matching the query")
                    % {"verbose_name": queryset.model._meta.verbose_name}
                )

            return obj
