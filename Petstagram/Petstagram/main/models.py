import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.main.validators_custom import validate_only_letters, ValidatePhotoMaxSizeMb


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    NO_SHOW = 'Do not show'
    GENDERS = [
        (MALE, MALE),
        (FEMALE, FEMALE),
        (NO_SHOW, NO_SHOW),
    ]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LENGTH),
                    validate_only_letters,
                    ),
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(LAST_NAME_MIN_LENGTH),
                    validate_only_letters,
                    ),
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        verbose_name='Link to Profile Picture',
    )

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
        null=True,
        blank=True,
        max_length=max([len(c[0]) for c in GENDERS]),
        choices=GENDERS,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    MAX_NAME_LENGTH = 30

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    TYPES = [
        (CAT, CAT),
        (DOG, DOG),
        (BUNNY, BUNNY),
        (PARROT, PARROT),
        (FISH, FISH),
        (OTHER, OTHER),
    ]

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Pet Name'
    )

    type = models.CharField(
        max_length=max(len(c[0]) for c in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Day of Birth'
    )

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        date_now = datetime.date.today().year
        birthday = self.date_of_birth.year
        return date_now - birthday

    def __str__(self):
        return f'{self.name} {self.type}'

    class Meta:
        unique_together = ('user_profile', 'name')


class PetsPhoto(models.Model):
    PHOTO_MAX_SIZE_MB = 5

    photo = models.ImageField(
        validators=(
            ValidatePhotoMaxSizeMb(PHOTO_MAX_SIZE_MB),
        )
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return f'Photos to {self.tagged_pets}'

    class Meta:
        ordering = ('likes', 'date_and_time_of_publication')
