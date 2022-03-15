from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATOR_ERROR_LETTERS_AND_UNDERSCORES = "Ensure this value contains only letters, numbers, and underscore."


def validate_only_letters_and_underscores(value):
    for symbol in value:
        if not symbol.isalpha() and not symbol == '_':
            raise ValidationError(VALIDATOR_ERROR_LETTERS_AND_UNDERSCORES)
