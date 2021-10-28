from rest_framework import viewsets, mixins
from rest_framework.response import Response
from ..models import Cohort

from ..serializers import CohortSerializer


class CohortViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer

    def list(self, request, *args, **kwargs):
        queryset = Cohort.objects.all()
        serializer = CohortSerializer(queryset, many=True)
        return Response(serializer.data)
