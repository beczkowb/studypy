from django.contrib.auth import get_user_model

from . import models

tag1 = models.ResourceTag.objects.create(name='python')
tag2 = models.ResourceTag.objects.create(name='django')
tag3 = models.ResourceTag.objects.create(name='javascript')
tag4 = models.ResourceTag.objects.create(name='react')
tag5 = models.ResourceTag.objects.create(name='beginner')
tag6 = models.ResourceTag.objects.create(name='best practises')
tag7 = models.ResourceTag.objects.create(name='websevelopment')
tag8 = models.ResourceTag.objects.create(name='html')
tag9 = models.ResourceTag.objects.create(name='css')

user = get_user_model().objects.create_user(username='admin',
                                            password='admin',
                                            email='admin@admin.com')

user2 = get_user_model().objects.create_user(username='beczkowb',
                                             password='admin2',
                                             email='admin2@admin.com')

tango = models.Resource.objects.create(name='Tango with Django',
                                       url='http://www.tangowithdjango.com/',
                                       description='A beginners guide to web development with Python 2.7 / Django 1.7',
                                       added_by=user)

hitguide = models.Resource.objects.create(
    name='The Hitchhiker’s Guide to Python!',
    url='http://www.docs.python-guide.org',
    description="""This opinionated guide exists to provide both novice and expert Python developers a best practice handbook to the installation, configuration, and usage of Python on a daily basis.""",
    added_by=user)

hitguide.tags.add(*[tag1, tag5, tag6])
hitguide.save()

w3 = models.Resource.objects.create(name='w3schools',
                                    url='http://www.w3schools.com',
                                    description='Web developmnet related tutorials',
                                    added_by=user2)

w3.tags.add(*[tag3, tag7, tag6, tag8, tag9])
w3.save()

reacttut = models.Resource.objects.create(name='reactjs tutorial',
                                          url='https://facebook.github.io/react/docs/tutorial.html',
                                          description='Great entry level tutorial for reactjs',
                                          added_by=user)
