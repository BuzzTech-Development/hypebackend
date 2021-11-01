from rest_framework import serializers
from django.contrib.auth.models import User

from .profile_serializer import ProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'pk',
            'date_joined',
            'email',
            'first_name',
            'last_name',
            'profile',
            'username'
        )
