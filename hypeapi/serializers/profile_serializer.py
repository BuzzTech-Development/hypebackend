from rest_framework import serializers

from ..models import Profile
from .cohort_serializer import CohortSerializer


class ProfileSerializer(serializers.ModelSerializer):
    cohorts = CohortSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('role', 'cohorts')
