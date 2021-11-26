import os
from django.core.exceptions import ValidationError


class FileExtensionValidator:
    def __init__(self, valid_extensions):
        self.valid_extensions = valid_extensions

    def __call__(self, value):
        ext = os.path.splitext(value.name)[1]

        if not ext.lower() in self.valid_extensions:
            raise ValidationError('Unsupported file extension.')
