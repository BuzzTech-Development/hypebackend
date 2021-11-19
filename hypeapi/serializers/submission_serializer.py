from rest_framework import serializers

from ..models import Submission, Upload
from .upload_serializer import UploadSerializer


class SubmissionSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()

    def get_files(self, obj):
        files = Upload.objects.filter(submission=obj)
        return UploadSerializer(files, many=True, read_only=False).data

    class Meta:
        model = Submission
        fields = ('__all__')
