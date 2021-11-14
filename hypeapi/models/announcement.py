from django.db import models
from .cohort import Cohort


class Announcement(models.Model):
    subject = models.CharField(max_length=200)
    text = models.TextField()
    cohort = models.ForeignKey(
        Cohort,
        on_delete=models.CASCADE,
        related_name='cohort'
    )