from rest_framework import serializers

from ..models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('__all__')
        read_only_fields = ('author')
