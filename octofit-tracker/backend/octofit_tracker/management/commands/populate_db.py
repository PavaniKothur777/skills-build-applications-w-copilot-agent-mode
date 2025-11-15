from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-11-15')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-11-14')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2025-11-13')
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date='2025-11-12')

        # Create workouts
        workout1 = Workout.objects.create(name='Hero Training', description='Intense workout for heroes')
        workout1.suggested_for.add(users[0], users[1])
        workout2 = Workout.objects.create(name='Justice League Prep', description='Team-based workout')
        workout2.suggested_for.add(users[2], users[3])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=175)
        Leaderboard.objects.create(team=dc, points=160)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
