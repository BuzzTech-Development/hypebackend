from rest_framework import viewsets
from rest_framework.response import Response

from ..models import Announcement
from ..serializers import AnnouncementSerializer
from ..utils import get_cohort_from_request


class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()

    def list(self, request, *args, **kwargs):
        cohort = get_cohort_from_request(request)
        queryset = self.queryset.filter(cohort=cohort)
        serializer = AnnouncementSerializer(queryset, many=True)
        return Response(serializer.data)
