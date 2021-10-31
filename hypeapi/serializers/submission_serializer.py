from rest_framework import serializers

from ..models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = (
            'id',
            'assignment',
            'comments',
            'points',
            'student',
            'time'
        )
