from django.utils import timezone
from rest_framework.exceptions import ValidationError


def year_validator(value):
    if value < 1895 or value > timezone.now().year:
        raise ValidationError(
            f'{value} is not a correcrt year!',
            params={'value': value},
        )
