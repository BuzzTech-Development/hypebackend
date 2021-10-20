from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile, Assignment, Meeting


class ProfileSerializer(serializers.ModelSerializer):
    cohorts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('role', 'cohorts')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'date_joined', 'profile',)


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('name', 'creationDateTime', 'description', 'points',
                  'badge', 'dueDateTime' 'graded', 'grade', 'numFiles', 'file')


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'name', 'cohort', 'date',
                  'start_time', 'end_time', 'link',)
