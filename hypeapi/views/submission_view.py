from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Submission
from ..serializers import SubmissionSerializer


class SubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        return Submission.objects.filter(author=self.request.user)
