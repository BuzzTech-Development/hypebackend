from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import Announcement, Cohort


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


@receiver(post_save, sender=Meeting)
def create_announcement(sender, instance, created, **kwargs):
    if created:
        Announcement.objects.create(
            subject=f'New meeting "{instance.name}" created',
            text=instance.link,
            cohort=instance.cohort
        )