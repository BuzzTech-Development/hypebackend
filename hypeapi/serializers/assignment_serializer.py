from rest_framework import serializers

from ..models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'badge',
            'creationDateTime',
            'description',
            'dueDateTime',
            'grade',
            'graded',
            'name',
            'numFiles',
            'points',
            'undated'
        )
