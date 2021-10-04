from django.shortcuts import render

from rest_framework import viewsets

from .serializers import AssignmentSerializer
from .models import Assignment


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all().order_by('name')
    serializer_class = AssignmentSerializer
