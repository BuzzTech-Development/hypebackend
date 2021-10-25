from django.db import models


class Assignment(models.Model):
    badge = models.IntegerField(default=-1, blank=True)
    creationDateTime = models.DateTimeField(default='2021-1-1 12:00')
    description = models.CharField(default='', max_length=1000)
    dueDateTime = models.DateTimeField(default='2021-1-1 12:00')
    grade = models.FloatField(default=0.0, null=True)
    graded = models.BooleanField(default=False)
    name = models.CharField(default='', max_length=30)
    numFiles = models.IntegerField(default=1)
    points = models.IntegerField(default=0)
    undated = models.BooleanField(default=False)

    def __str__(self):
        return self.name
