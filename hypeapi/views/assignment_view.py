from django.db.models import Q

from rest_framework import viewsets

from ..models import Assignment
from ..serializers import AssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        user_cohorts = self.request.user.profile.cohorts.all()
        return Assignment.objects.filter(cohort__in=user_cohorts)
