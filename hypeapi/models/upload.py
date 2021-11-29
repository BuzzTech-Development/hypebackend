from django.db import models

from hypeapi.models import submission

from ..validators import FileExtensionValidator
from . import Submission


class Upload(models.Model):
    file = models.FileField()
    submission = models.ForeignKey(
        Submission, related_name='uploads', on_delete=models.CASCADE)

    def __str__(self):
        return f'Submission {self.id}'
