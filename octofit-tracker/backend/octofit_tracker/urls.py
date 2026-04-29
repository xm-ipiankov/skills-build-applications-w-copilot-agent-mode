from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import TeamViewSet, UserProfileViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardEntryViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserProfileViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'teams': reverse('team-list', request=request, format=format),
        'users': reverse('userprofile-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
        'leaderboard': reverse('leaderboardentry-list', request=request, format=format),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]