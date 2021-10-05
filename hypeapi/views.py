from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserSerializer, AssignmentSerializer
from .models import Assignment


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all().order_by('name')
    serializer_class = AssignmentSerializer
