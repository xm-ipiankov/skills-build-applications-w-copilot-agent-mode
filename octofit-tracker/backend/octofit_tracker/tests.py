from django.test import TestCase
from .models import Team, UserProfile, Activity, Workout, LeaderboardEntry

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_userprofile_creation(self):
        team = Team.objects.create(name='Test Team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, date='2024-01-01')
        self.assertIn('Run', str(activity))

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team')
        workout = Workout.objects.create(name='Pushups')
        workout.suggested_for.add(team)
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_entry_creation(self):
        team = Team.objects.create(name='Test Team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        entry = LeaderboardEntry.objects.create(user=user, score=100, rank=1)
        self.assertIn('Rank 1', str(entry))
