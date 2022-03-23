import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.Web.validators import validate_only_letters


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30
    MIN_FIRST_NAME_LENGTH = 2
    MIN_LAST_NAME_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    MAX_GENDER_LENGTH = max([len(x[0]) for x in GENDERS])

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(MinLengthValidator(MIN_FIRST_NAME_LENGTH),
                    validate_only_letters,
                    ),
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(MinLengthValidator(MIN_LAST_NAME_LENGTH),
                    validate_only_letters,
                    ),
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=MAX_GENDER_LENGTH,
        choices=GENDERS,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    MAX_LENGTH_NAME = 30

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [(a, a) for a in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    @property
    def years(self):
        return datetime.date.today().year - self.date_of_bird.year

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
    )

    types = models.CharField(
        max_length=max([len(x[0]) for x in TYPES]),
        choices=TYPES,
    )

    date_of_bird = models.DateField(
        null=True,
        blank=True,
    )

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('user_profile', 'name')

    def __str__(self):
        return f'{self.name} - {self.types}'


class PetsPhoto(models.Model):
    MAX_PHOTO_SIZE_MB = 5

    photo = models.ImageField(
        # validators=(validate_max_size(MAX_PHOTO_SIZE_MB),
        #             ),
    )

    tagged = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    date_time_publication = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,

    )
