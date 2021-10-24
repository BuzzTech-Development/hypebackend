from django.db import models


class Assignment(models.Model):
    name = models.CharField(max_length=30)
    creationDateTime = models.DateTimeField()
    description = models.CharField(max_length=1000)
    points = models.IntegerField()
    badge = models.IntegerField(blank=True, default=0)
    dueDateTime = models.DateTimeField()
    graded = models.BooleanField()
    grade = models.FloatField(null=True)
    numFiles = models.IntegerField()
    file = models.FileField()

    def __str__(self):
        return self.name
