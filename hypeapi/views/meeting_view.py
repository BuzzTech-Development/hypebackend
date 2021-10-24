from rest_framework import viewsets, status
from rest_framework.response import Response

from models import Meeting
from serializers import MeetingSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def list(self, request, *args, **kwargs):
        print(request.query_params)
        cohort = request.query_params.get('cohort', None)
        if not cohort:
            return Response(
                {'status': 'Required parameter cohort not provide'},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = self.queryset.filter(cohort=cohort)
        serializer = MeetingSerializer(queryset, many=True)
        return Response(serializer.data)
