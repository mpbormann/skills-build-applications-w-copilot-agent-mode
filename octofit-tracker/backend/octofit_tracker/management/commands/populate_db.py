from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users
        users = [
            User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel),
            User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel),
            User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc),
            User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Super Strength', description='Strength workout', difficulty='Hard'),
            Workout.objects.create(name='Flight Training', description='Flight skills', difficulty='Medium'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Strength', duration=60, date=timezone.now())
        Activity.objects.create(user=users[1], type='Cardio', duration=45, date=timezone.now())
        Activity.objects.create(user=users[2], type='Stealth', duration=30, date=timezone.now())
        Activity.objects.create(user=users[3], type='Flight', duration=50, date=timezone.now())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=95)
        Leaderboard.objects.create(user=users[3], score=85)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
