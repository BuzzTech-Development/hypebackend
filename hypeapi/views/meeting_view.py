from rest_framework import viewsets, status
from rest_framework.response import Response

from ..models import Meeting
from ..serializers import MeetingSerializer
from ..utils import get_cohort_from_request


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def list(self, request, *args, **kwargs):
        cohort = get_cohort_from_request(request)

        queryset = self.queryset.filter(cohort=cohort)
        serializer = MeetingSerializer(queryset, many=True)
        return Response(serializer.data)
