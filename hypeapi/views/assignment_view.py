from rest_framework.response import Response
from rest_framework import status, viewsets

from ..models import Assignment
from ..serializers import AssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        user_cohorts = self.request.user.profile.cohorts.all()
        return Assignment.objects.filter(cohort__in=user_cohorts)
