from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile, Assignment


class ProfileSerializer(serializers.ModelSerializer):
    cohorts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('role', 'cohorts')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'profile')


class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        fields = ('name', 'grade')
