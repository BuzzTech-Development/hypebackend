from django.db import models
from .cohort import Cohort


class Announcement(models.Model):
    subject = models.CharField(max_length=200)
    text = models.TextField()
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
