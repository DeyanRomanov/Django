from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator
from django.db import models

from musciapp.main.validators import validate_only_letters_and_underscores


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 30

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(MinLengthValidator(USERNAME_MIN_LENGTH),
                    validate_only_letters_and_underscores,
                    ),
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(MinValueValidator(AGE_MIN_VALUE),
                    ),
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30

    ARTISTS_MAX_LENGTH = 30

    GENRE_MAX_LENGTH = 30

    PRICE_MIN_VALUE = 0
    PRICE_DECIMAL_PLACES = 2

    POP = "Pop Music"
    JAZZ = "Jazz Music"
    R_AND_B = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"
    GENRE_CHOICE = [
        (POP, POP),
        (JAZZ, JAZZ),
        (R_AND_B, R_AND_B),
        (ROCK, ROCK),
        (COUNTRY, COUNTRY),
        (DANCE, DANCE),
        (HIP_HOP, HIP_HOP),
        (OTHER, OTHER),
    ]
    name = models.CharField(
        max_length=ALBUM_NAME_MAX_LENGTH,
        unique=True,
        validators=(MaxLengthValidator(ALBUM_NAME_MAX_LENGTH),
                    ),
    )

    artist = models.CharField(
        max_length=ARTISTS_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=ALBUM_NAME_MAX_LENGTH,
        choices=GENRE_CHOICE,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(MinValueValidator(PRICE_MIN_VALUE),
                    ),
    )

    class Meta:
        ordering = (
            'id',
            'price',
        )
