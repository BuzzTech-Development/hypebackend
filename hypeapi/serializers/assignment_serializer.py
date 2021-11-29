from rest_framework import serializers

from ..models import Assignment, Submission


class AssignmentSerializer(serializers.ModelSerializer):
    submissions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Assignment
        fields = ('__all__')
        read_only_fields = ['author']
