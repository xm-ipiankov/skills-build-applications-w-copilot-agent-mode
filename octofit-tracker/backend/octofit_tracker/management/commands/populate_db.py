from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, UserProfile, Activity, Workout, LeaderboardEntry
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        tony = UserProfile.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel, is_leader=True)
        steve = UserProfile.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = UserProfile.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc, is_leader=True)
        clark = UserProfile.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, activity_type='Iron Suit Training', duration=60, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='Shield Practice', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='Martial Arts', duration=90, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='Flight', duration=120, date=timezone.now().date())

        # Create Workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        workout2 = Workout.objects.create(name='Agility Drills', description='Agility and reflex training')
        workout1.suggested_for.add(marvel, dc)
        workout2.suggested_for.add(marvel, dc)

        # Create Leaderboard Entries
        LeaderboardEntry.objects.create(user=tony, score=150, rank=1)
        LeaderboardEntry.objects.create(user=steve, score=120, rank=2)
        LeaderboardEntry.objects.create(user=bruce, score=110, rank=3)
        LeaderboardEntry.objects.create(user=clark, score=100, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
