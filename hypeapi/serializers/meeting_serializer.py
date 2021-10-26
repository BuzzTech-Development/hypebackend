from rest_framework import serializers

from ..models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = (
            'cohort',
            'date',
            'end_time',
            'link',
            'name',
            'start_time'
        )
