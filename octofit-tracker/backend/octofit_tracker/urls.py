from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import TeamViewSet, UserProfileViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardEntryViewSet

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse
import os

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserProfileViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)


@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        scheme = 'https' if request.is_secure() else 'http'
        base_url = f"{scheme}://{request.get_host()}"
    return Response({
        'teams': base_url + reverse('team-list'),
        'users': base_url + reverse('userprofile-list'),
        'activities': base_url + reverse('activity-list'),
        'workouts': base_url + reverse('workout-list'),
        'leaderboard': base_url + reverse('leaderboardentry-list'),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]