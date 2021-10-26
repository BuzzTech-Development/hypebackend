from django.db import models
from django.contrib.auth.models import User

from .cohort import Cohort


class Profile(models.Model):
    """A profile to be associated with a single user containing extra role information"""

    cohorts = models.ManyToManyField(Cohort)
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

    def __str__(self):
        return f'{self.user.username} profile'
