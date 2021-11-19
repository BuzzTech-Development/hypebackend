from django.urls import include, path
from rest_framework import routers

from .views import AssignmentViewSet, MeetingViewSet, SubmissionViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'assignments', AssignmentViewSet, basename='Assignment')
router.register(r'meetings', MeetingViewSet, basename='Meeting')
router.register(r'submissions', SubmissionViewSet, basename='Submission')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
