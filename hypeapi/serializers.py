from rest_framework import serializers

from .models import Assignment


class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        fields = ('name', 'grade')
