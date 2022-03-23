from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for symbol in value:
        if not symbol.isalpha():
            raise ValidationError('It should consist only of letters')


def validate_max_size(max_size_in_mb):
    def validate_size(photo):
        photo_size = photo.file.size
        limit_size_kb = max_size_in_mb * 1024 * 1024
        if limit_size_kb < photo_size:
            raise ValidationError(f'Max file size is {max_size_in_mb} MB')
    return validate_size
