from rest_framework import serializers

from ..models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'name', 'cohort', 'date',
                  'start_time', 'end_time', 'link',)
