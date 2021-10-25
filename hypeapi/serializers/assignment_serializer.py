from rest_framework import serializers

from ..models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'badge',
            'creation_date_time',
            'description',
            'due_date_time',
            'name',
            'num_files',
            'points'
        )
