
from django.core.validators import RegexValidator
from django.conf import settings

NAME_REGEX = RegexValidator(r'^[a-zA-Z_ ]*$', 'Invalid characters')