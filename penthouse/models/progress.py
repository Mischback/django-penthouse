# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Models needed for progress planning."""

# Django imports
from django import forms
from django.db import models
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

# app imports
from penthouse.exceptions import PenthouseModelException
from penthouse.game_constants import MilestoneResource
from penthouse.models.profile import Profile


class ProgressModelException(PenthouseModelException):
    """Base class for all exceptions related to ``Progress`` models."""


class MilestoneManager(models.Manager):
    """Custom manager for ``ProgressMilestone`` model."""

    def get_queryset(self):
        """Annotate the object with the count of related objects."""
        return (
            super()
            .get_queryset()
            .annotate(
                total_sections=Count("milestone_sections"),
                total_steps=Count("milestone_sections__milestone_steps"),
            )
        )

    def filter_by_user(self, user=None):
        """Filter the milestones by the specified user."""
        if user is None:
            raise ProgressModelException("No user specified!")

        return self.get_queryset().filter(profile__owner=user)


class Milestone(models.Model):
    """A single milestone to reach."""

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name=_("Profile")
    )
    """Reference to the associated profile."""

    title = models.CharField(
        help_text=_("Title of this milestone"), verbose_name=_("Title"), max_length=255
    )
    """Title of this milestone."""

    date_added = models.DateTimeField(
        help_text=_("Date this milestone was added"), verbose_name=_("Date of creation")
    )

    date_completed = models.DateField(
        help_text=_("Date this milestone was completed"),
        verbose_name=_("Date of completion"),
        null=True,
        blank=True,
    )

    objects = MilestoneManager()
    """Apply a custom manager.

    This should not interfere with Django's default inner mechanics, the
    custom manager does not replace any default functions, it just provides
    additional methods.
    """

    class Meta:  # noqa: D106
        app_label = "penthouse"
        verbose_name = _("Progress Planning Milestone")
        verbose_name_plural = _("Progress Planning Milestones")

    def __str__(self):  # noqa: D105
        return "[Milestone] {}".format(self.title)


class MilestoneForm(forms.ModelForm):
    """Used to validate input for creating and updating ``Milestone`` instances."""

    class Meta:  # noqa: D106
        model = Milestone
        fields = ["title", "date_added"]


class MilestoneSection(models.Model):
    """One dedicated section of a ``Milestone``."""

    milestone = models.ForeignKey(
        Milestone,
        on_delete=models.CASCADE,
        related_name="milestone_sections",
        verbose_name=_("Milestone Section"),
    )
    """Reference to the parent ``Milestone`` instance."""

    caption = models.CharField(
        help_text=_("Caption of this section"),
        verbose_name=_("Section"),
        max_length=255,
    )

    resource = models.CharField(
        help_text=_("Required resource"),
        verbose_name=_("Resource"),
        choices=MilestoneResource,
        max_length=5,
    )

    class Meta:  # noqa: D106
        app_label = "penthouse"
        verbose_name = _("Progress Planning Section")
        verbose_name_plural = _("Progress Planning Sections")

    def __str__(self):  # noqa: D105
        return "[Section] {}".format(self.caption)


class MilestoneSectionForm(forms.ModelForm):
    """Used to validate input for creating and updating ``MilestoneSection`` instances."""

    class Meta:  # noqa: D106
        model = MilestoneSection
        fields = ["caption", "resource"]


class MilestoneStep(models.Model):
    """A single step of a ``MilestoneSection``."""

    section = models.ForeignKey(
        MilestoneSection,
        on_delete=models.CASCADE,
        related_name="milestone_steps",
        verbose_name=_("Milestone Step"),
    )
    """Reference to the parent ``MilestoneSection`` instance. """

    step_value = models.CharField(
        help_text=_("Value of this step"),
        verbose_name=_("Value"),
        max_length=50,
        default="0",
    )

    completed = models.BooleanField(
        help_text=_("Determine if this step is already completed"),
        verbose_name=_("step completion status"),
        default=False,
    )

    class Meta:  # noqa: D106
        app_label = "penthouse"
        verbose_name = _("Progress Planning Step")
        verbose_name_plural = _("Progress Planning Step")

    def __str__(self):  # noqa: D105
        return "[Step] {}".format(self.caption)


class MilestoneStepForm(forms.ModelForm):
    """Used to validate input for creating and updating ``MilestoneSection`` instances."""

    class Meta:  # noqa: D106
        model = MilestoneStep
        fields = ["step_value"]
