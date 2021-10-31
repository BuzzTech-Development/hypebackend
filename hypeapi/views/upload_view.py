from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Upload
from ..serializers import UploadSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

    def list(self, request, *args, **kwargs):
        queryset = Upload.objects.all()
        serializer = UploadSerializer(queryset, many=True)
        return Response(serializer.data)
