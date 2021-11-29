from rest_framework import serializers

from ..models import Assignment
from .submission_serializer import SubmissionSerializer


class AssignmentSerializer(serializers.ModelSerializer):
    submissions = SubmissionSerializer(many=True, read_only=True)

    class Meta:
        model = Assignment
        fields = ('__all__')
        read_only_fields = ['author']
