from django.db import models
from django.utils import timezone

from .cohort import Cohort


class Assignment(models.Model):
    '''
        Represents an assignment created by an instructor and given to a cohort.
    '''
    badge = models.IntegerField(default=-1)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(default='', max_length=1000)
    due_date = models.DateTimeField(default=timezone.now)
    file_extensions = models.JSONField(default=list)
    name = models.CharField(default='', max_length=30)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
