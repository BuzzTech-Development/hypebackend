from django.db import models


class Assignment(models.Model):
    name = models.CharField(max_length=60)
    grade = models.FloatField()

    def __str__(self):
        return self.name
