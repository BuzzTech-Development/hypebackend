from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Assignment
from ..serializers import AssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def list(self, request, *args, **kwargs):
        queryset = Assignment.objects.all()
        serializer = AssignmentSerializer(queryset, many=True)
        return Response(serializer.data)
