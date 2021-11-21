from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import Announcement


class Assignment(models.Model):
    '''
        Represents an assignment created by an instructor and given to a cohort.
    '''
    badge = models.IntegerField(default=-1)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(default='', max_length=1000)
    due_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(default='', max_length=30)
    num_files = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

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
