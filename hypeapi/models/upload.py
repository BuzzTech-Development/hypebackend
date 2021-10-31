from django.db import models

from . import Submission


class Upload(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    file = models.FileField()
    file_type = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.file_type
