from django.db import models
from django.utils import timezone


class Assignment(models.Model):
    '''
        Represents an assignment created by an instructor and given to a cohort.
    '''

    badge = models.IntegerField(default=-1)
    creation_date_time = models.DateTimeField(default=timezone.now())
    description = models.CharField(default='', max_length=1000)
    due_date_time = models.DateTimeField(default=timezone.now())
    name = models.CharField(default='', max_length=30)
    num_files = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
