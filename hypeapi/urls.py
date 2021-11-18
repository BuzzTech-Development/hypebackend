from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

from .views import AssignmentViewSet, MeetingViewSet, UserViewSet, CohortViewSet

router = routers.DefaultRouter()
router.register(r'assignments', AssignmentViewSet)
router.register(r'meetings', MeetingViewSet)
router.register(r'user', UserViewSet)
router.register(r'cohorts', CohortViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-verify/', verify_jwt_token),
    path('api-token-refresh/', refresh_jwt_token)
]
