from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Assignment, Submission
from ..serializers import SubmissionSerializer, UploadSerializer


class SubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        author = Assignment.objects.get(id=data['assignment']).author

        if 'points' in data and request.user is not author:
            return Response('Points can only be updated by assignment author.',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        if self.request.user.profile.role == 'INSTRUCTOR':
            return Submission.objects.all()
        else:
            return Submission.objects.filter(author=self.request.user)
