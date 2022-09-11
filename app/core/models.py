"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _

from core.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name=_('email'),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('staff'),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('active'),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
