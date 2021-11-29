from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

from hypeapi.views.cohort_view import CohortViewSet

from .views import AnnouncementViewSet, AssignmentViewSet, MeetingViewSet, SubmissionViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementViewSet)
router.register(r'assignments', AssignmentViewSet, basename='Assignment')
router.register(r'meetings', MeetingViewSet, basename='Meeting')
router.register(r'submissions', SubmissionViewSet, basename='Submission')
router.register(r'users', UserViewSet)
router.register(r'cohorts', CohortViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-verify/', verify_jwt_token),
    path('api-token-refresh/', refresh_jwt_token)
]
