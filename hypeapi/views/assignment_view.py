from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Assignment
from ..serializers import AssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def list(self, request, *args, **kwargs):
        cohort = request.query_params.get('cohort', None)
        if not cohort:
            return Response(
                {'status': 'Required parameter cohort not provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = self.queryset.filter(cohort=cohort)
        serializer = AssignmentSerializer(queryset, many=True)
        return Response(serializer.data)
