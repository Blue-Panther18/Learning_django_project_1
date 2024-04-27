import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProTwo.settings')

import django
django.setup()

## FAKE POP SCRIPT

import random
from AppTwo.models import User
from faker import Faker

fake_gen = Faker()

def populate(N=10):
    for entry in range(N):

        # Create a fake user data for the entry
        fake_first_name = fake_gen.unique.first_name()
        fake_last_name = fake_gen.unique.last_name()
        fake_email = fake_gen.email()

        # Create the new user entry
        user_details = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print('Populating Script!')
    populate(40)
    print('Populating complete!')