from django.db import models

from ..validators import FileExtensionValidator
from . import Submission


class Upload(models.Model):
    file = models.FileField()
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_type
