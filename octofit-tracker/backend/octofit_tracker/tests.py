from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team2', description='A test team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'test@example.com')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team3', description='A test team')
        user = User.objects.create(name='Test User2', email='test2@example.com', team=team)
        lb = Leaderboard.objects.create(user=user, score=42)
        self.assertEqual(str(lb), 'test2@example.com - 42')
