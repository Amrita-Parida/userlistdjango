from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime,timedelta
import random, string
from usermanagement.models import *

def randomword():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(6))

class Command(BaseCommand):
    help = 'Create random users'
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            user = MyUser.objects.create(user_name=randomword())
            user.set_password('123')
            user.save()
            ActivityPeriod.objects.create(user=user,start_time=datetime.today(),
                                                    end_time=datetime.today() + timedelta(minutes= 60))
            print(user)