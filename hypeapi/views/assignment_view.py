import operator
from functools import reduce

from django.db.models import Q

from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Assignment
from ..serializers import AssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        user_cohorts = self.request.user.profile.cohorts.all()
        query = (Q(cohorts__id__contains=cohort.id) for cohort in user_cohorts)
        return Assignment.objects.filter(reduce(operator.or_, query))
