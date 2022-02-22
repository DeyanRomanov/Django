from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from djangoProject1.web.custom_validators import validate_only_letter, ValidateImageMaxSizeInMb, \
    validate_positive_number


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2

    MIN_BUDGET = 0
    BUDGET_DEFAULT = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    DIR_TO_UPLOAD_MEDIA_FILES = 'media/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        verbose_name='First Name',
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letter,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        verbose_name='Last Name',
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letter,
        ),
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT,
        validators=(
            MinValueValidator(MIN_BUDGET),
        ),
    )

    profile_image = models.ImageField(
        upload_to=DIR_TO_UPLOAD_MEDIA_FILES,
        null=True,
        blank=True,
        verbose_name='Profile Image',
        validators=(
            ValidateImageMaxSizeInMb(IMAGE_MAX_SIZE_IN_MB),
        ),
    )


class Expense(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    expense_image = models.URLField(
        verbose_name='Link to Image'
    )

    price = models.FloatField(
        validators=(
            validate_positive_number,
        ),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('title', 'price')
