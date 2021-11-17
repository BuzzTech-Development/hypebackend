from django.urls import include, path
from rest_framework import routers

from .views import AssignmentViewSet, MeetingViewSet, UploadViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'assignments', AssignmentViewSet, basename='Assignment')
router.register(r'meetings', MeetingViewSet)
router.register(r'submission', UploadViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
