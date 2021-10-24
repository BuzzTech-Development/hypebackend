from rest_framework import serializers

from models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('name', 'creationDateTime', 'description', 'points',
                  'badge', 'dueDateTime' 'graded', 'grade', 'numFiles', 'file')
