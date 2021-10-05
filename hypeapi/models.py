from django.db import models
from django.contrib.auth.models import User


class Cohort(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    """A profile to be associated with a single user containing extra role information"""
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

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

    cohorts = models.ManyToManyField(Cohort)

    def __str__(self):
        return f'{self.user.username} profile'


class Assignment(models.Model):
    name = models.CharField(max_length=60)
    grade = models.FloatField()

    def __str__(self):
        return self.name
