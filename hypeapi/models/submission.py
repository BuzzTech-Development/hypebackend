from django.contrib.auth.models import User
from django.db import models

from . import Assignment


class Submission(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, blank=True, default='')
    graded = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comments
