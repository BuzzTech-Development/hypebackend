from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Submission
from ..serializers import SubmissionSerializer, UploadSerializer


class SubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(author=self.request.user)

        if request.FILES:
            files = dict((request.FILES).lists()).get('files', None)
            if files:
                for file in files:
                    file_data = {}
                    file_data['submission'] = instance.pk
                    file_data['file'] = file
                    upload_serializer = UploadSerializer(data=file_data)
                    upload_serializer.is_valid(raise_exception=True)
                    upload_serializer.save()
        return Response(serializer.data)

    def get_queryset(self):
        return Submission.objects.filter(author=self.request.user)
