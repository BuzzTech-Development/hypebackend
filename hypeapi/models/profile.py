from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .cohort import Cohort


class Profile(models.Model):
    """A profile to be associated with a single user containing extra role information"""

    cohorts = models.ManyToManyField(Cohort, blank=True)
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )
    user_roles = [
        ('ADMIN', 'Admin'),
        ('INSTRUCTOR', 'Instructor'),
        ('STUDENT', 'Student'),
        ('PARENT', 'Parent'),
    ]
    role = models.CharField(
        max_length=15,
        choices=user_roles,
        default='STUDENT'
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'
