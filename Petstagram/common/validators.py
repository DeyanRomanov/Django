from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

ONLY_LETTERS_VALIDATION_ERROR_MESSAGE = 'This field should consist only of letters'


def validate_only_letters(value):
    for symbol in value:
        if not symbol.isalpha():
            return ValidationError(ONLY_LETTERS_VALIDATION_ERROR_MESSAGE)


@deconstructible
class MaxFileSizeInMbValidator:
    EXCEPTION_MESSAGE = 'Photo maximum size of the photo can be'

    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(f'{self.EXCEPTION_MESSAGE} {self.max_size}MB')
