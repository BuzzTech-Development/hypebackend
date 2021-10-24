from django.db import models

from .cohort import Cohort


class Meeting(models.Model):
    name = models.CharField(max_length=50)
    cohort = models.ForeignKey(
        Cohort, related_name='cohort', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    link = models.TextField()

    def __str__(self):
        return self.name
