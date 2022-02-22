from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATION_ERROR_MESSAGE_ONLY_LETTERS = "Ensure this value contains only letters."
VALIDATION_ERROR_MESSAGE_POSITIVE_NUMBERS = "Budget can not be below 0"


def validate_only_letter(value):
    if not value.isalpha():
        raise ValidationError(VALIDATION_ERROR_MESSAGE_ONLY_LETTERS)


@deconstructible
class ValidateImageMaxSizeInMb:
    __CONVERT_MB_TO_BYTES = 1024 * 1024

    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * self.__CONVERT_MB_TO_BYTES:
            raise ValidationError(self.validation_error_message())

    def validation_error_message(self):
        error_message = f"Max file size is {self.max_size:.2f} MB"
        return error_message


def validate_positive_number(value):
    if value < 0:
        raise ValidationError(VALIDATION_ERROR_MESSAGE_POSITIVE_NUMBERS)
