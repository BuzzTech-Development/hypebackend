from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User

from .announcement import Announcement
from .cohort import Cohort


class Assignment(models.Model):
    '''
        Represents an assignment created by an instructor and given to a cohort.
    '''

    author = models.ForeignKey(
        User,
        related_name='authors',
        on_delete=models.CASCADE,
    )
    badge = models.IntegerField(blank=True, null=True)
    cohort = models.ForeignKey(
        Cohort,
        related_name='cohorts',
        on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000, blank=True)
    due_date = models.DateTimeField(default=timezone.now)
    file_extensions = models.JSONField(blank=True, null=True)
    name = models.CharField(max_length=50)
    points = models.IntegerField()

    def __str__(self):
        return self.name


@receiver(post_save, sender=Assignment)
def create_announcement(sender, instance, created, **kwargs):
    if created:
        Announcement.objects.create(
            subject=f'New assignment "{instance.name}" created',
            text=instance.description,
            cohort=instance.cohort
        )
