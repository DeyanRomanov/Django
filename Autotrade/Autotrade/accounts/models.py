from django.contrib.auth import models as auth_models
from django.contrib.auth import base_user
from django.db import models

from Autotrade.accounts.managers import UserAccountManager


class UserAccount(base_user.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = UserAccountManager()
