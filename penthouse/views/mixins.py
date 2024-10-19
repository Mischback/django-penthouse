# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""App-specific mixins to be used with class-based views."""

# Django imports
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.utils.translation import gettext_lazy as _

# app imports
from penthouse.models.profile import Profile


class ProfileIDMixin:
    """Injects the current user's profile ID into the context.

    This mixin can only be used on views that also use the
    ``LoginRequiredMixin``.
    """

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)

        context["profile_id"] = Profile.objects.get(owner=self.request.user).id

        return context


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
