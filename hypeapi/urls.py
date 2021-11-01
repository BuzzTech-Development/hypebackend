from django.urls import include, path
from rest_framework import routers

from .views import AssignmentViewSet, MeetingViewSet, UserViewSet, CohortViewSet

router = routers.DefaultRouter()
router.register(r'assignments', AssignmentViewSet)
router.register(r'meetings', MeetingViewSet)
router.register(r'user', UserViewSet)
router.register(r'cohorts', CohortViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
