from django.urls import include, path
from rest_framework import routers

from .views import AnnouncementViewSet, AssignmentViewSet, MeetingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'meetings', MeetingViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
