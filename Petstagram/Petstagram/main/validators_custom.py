from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATION_ERROR_ONLY_LETTERS_CONSIST = 'It should have at least 2 chars, max - 30 chars, and should consist only of letters.'


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError(VALIDATION_ERROR_ONLY_LETTERS_CONSIST)


@deconstructible
class ValidatePhotoMaxSizeMb:
    def __init__(self, maxsize):
        self.maxsize = maxsize

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.maxsize * 1024 * 1024:
            raise ValidationError("Max file size is " + f"{self.maxsize}")
