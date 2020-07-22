import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

# all of this done to setup faker cofiguration in settings before populating our models
# fake pop script
import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    # here i am basically adding zero because t created is a tuple and at first instance is object and at second position is what type of entry it is,
    # so i am grabbing the object part only by calling zero
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for entry
        top=add_topic()

        # create fake data for entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()


        # create new webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create fake AccessRecord for that webpage
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]



if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete')
