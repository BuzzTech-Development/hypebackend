from rest_framework import serializers

from ..models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'id',
            'badge',
            'cohorts',
            'creation_date',
            'description',
            'due_date',
            'name',
            'num_files',
            'points'
        )
