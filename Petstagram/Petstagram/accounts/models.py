from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.accounts.managers import PetstagramUserManager
from common.validators import validate_only_letters


class PetstagramUserModel(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 55

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [
        (MALE, MALE),
        (FEMALE, FEMALE),
        (DO_NOT_SHOW, DO_NOT_SHOW),
    ]
    GENDERS_MAX_LENGTH = max([len(x[0]) for x in GENDERS])

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        verbose_name='Link to Profile Picture'
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date of Birth'
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email_address = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        null=True,
        blank=True,
        max_length=GENDERS_MAX_LENGTH,
        choices=GENDERS,
        default=DO_NOT_SHOW
    )

    user = models.OneToOneField(
        PetstagramUserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
