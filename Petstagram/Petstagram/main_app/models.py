from django.contrib.auth import get_user_model
from django.db import models

from common.validators import MaxFileSizeInMbValidator

UserModel = get_user_model()


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    CAT = 'cat'
    DOG = 'dog'
    BUNNY = 'bunny'
    PARROT = 'parrot'
    FISH = 'fish'
    OTHER = 'other'
    TYPES = [
        (CAT, CAT),
        (DOG, DOG),
        (BUNNY, BUNNY),
        (PARROT, PARROT),
        (FISH, FISH),
        (OTHER, OTHER),
    ]
    TYPES_MAX_LENGTH = max([len(x[0]) for x in TYPES])

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name='Pet Name',
    )

    type = models.CharField(
        max_length=TYPES_MAX_LENGTH,
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date of Birth'
    )

    user_profile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = [
            'user_profile',
            'name',
        ]

    def __str__(self):
        return f'{self.name} - {self.type}'


class PetPhoto(models.Model):
    PHOTO_MAX_SIZE_MB = 5

    photo = models.ImageField(
        validators=(
            MaxFileSizeInMbValidator(PHOTO_MAX_SIZE_MB),
        ),
        verbose_name='Pet Image',
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    date_and_time = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.PositiveIntegerField(
        default=0,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        verbose_name='Tag Pets'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
