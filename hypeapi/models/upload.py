from django.db import models

from hypeapi.models import submission

from ..validators import FileExtensionValidator
from . import Submission


def update_filename(instance, filename):
    return f'{instance.submission.assignment.name}/{instance.submission.author.username}/{instance.submission.time}_{filename}'


class Upload(models.Model):
    file = models.FileField(upload_to=update_filename)
    submission = models.ForeignKey(
        Submission, related_name='uploads', on_delete=models.CASCADE)

    def __str__(self):
        return f'Submission {self.id}'
