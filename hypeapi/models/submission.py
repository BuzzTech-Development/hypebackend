from django.db import models
from django.utils import timezone

from . import Assignment, Profile


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, default="")
    points = models.IntegerField(default=0)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comments
