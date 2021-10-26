from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User

from ..serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
