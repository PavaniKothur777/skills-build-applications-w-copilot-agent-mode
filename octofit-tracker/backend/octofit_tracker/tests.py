from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2025-11-15')
        self.workout = Workout.objects.create(name='Hero Training', description='Intense workout for heroes')
        self.workout.suggested_for.add(self.user)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Running')
        self.assertEqual(self.activity.user.email, 'spiderman@marvel.com')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Hero Training')
        self.assertIn(self.user, self.workout.suggested_for.all())

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.team.name, 'Marvel')
        self.assertEqual(self.leaderboard.points, 100)
