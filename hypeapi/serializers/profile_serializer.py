from rest_framework import serializers

from models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    cohorts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('role', 'cohorts')
