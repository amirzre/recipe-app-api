"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.conf import settings
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


class Recipe(models.Model):
    """Recipe object."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name=_('user'),
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_('title'),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('description'),
    )
    time_minutes = models.IntegerField(
        verbose_name=_('time'),
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('price'),
    )
    link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='link',
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name=_('tags'),
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        verbose_name=_('ingredients'),
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Tag for fitering recipes."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tags',
        verbose_name=_('user'),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient for recipes."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ingredients',
        verbose_name=_('ingredient'),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )

    def __str__(self):
        return self.name
