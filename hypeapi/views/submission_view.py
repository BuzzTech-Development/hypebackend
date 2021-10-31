from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Submission
from ..serializers import SubmissionSerializer


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def list(self, request, *args, **kwargs):
        queryset = Submission.objects.all()
        serializer = SubmissionSerializer(queryset, many=True)
        return Response(serializer.data)
