from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserSerializer, AssignmentSerializer, MeetingSerializer
from .models import Assignment, Meeting


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


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
