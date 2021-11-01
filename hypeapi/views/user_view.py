from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User
from ..models import Profile
from rest_framework.decorators import action

from ..serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)


    # I'm pretty sure this is the wrong way to go about this, as far as the loop goes, but it works *shrugs*
    # Looking for suggestions
    @action(methods=['get'], detail=False, url_path='students', url_name='students')
    def list_students(self, request, *args, **kwargs):
        students = set()
        for profile in Profile.objects.filter(role='STUDENT').select_related('user'):
            students.add(User.objects.get(id=profile.user.id))

        serializer = UserSerializer(students, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='curr', url_name='curr')
    def curr_user(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
