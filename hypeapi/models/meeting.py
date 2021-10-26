from django.db import models

from .cohort import Cohort


class Meeting(models.Model):
    cohort = models.ForeignKey(
        Cohort,
        related_name='cohort',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    end_time = models.TimeField()
    link = models.TextField()
    name = models.CharField(max_length=50)
    start_time = models.TimeField()

    def __str__(self):
        return self.name
