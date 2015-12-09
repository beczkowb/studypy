from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db.utils import IntegrityError

from . import models as res_models


class TestReview(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='admin',
                                                         password='admin',
                                                         email='admin@admin.com')
        self.user2 = get_user_model().objects.create_user(username='admin2',
                                                          password='admin2',
                                                          email='admin2@admin.com')
        self.resource = res_models.Resource.objects.create(
            name='Tango with Django',
            url='http://www.tangowithdjango.com/',
            description='Cool django book',
            added_by=self.user)

    def test_save(self):
        review = res_models.Review.objects.create(resource=self.resource,
                                                  author=self.user,
                                                  contents='its nice',
                                                  mark=5)
        self.assertEqual(self.resource.rating, review.mark)
        review = res_models.Review.objects.create(resource=self.resource,
                                                  author=self.user2,
                                                  contents='its nice2',
                                                  mark=3)
        self.assertEqual(self.resource.rating, 4)
        with self.assertRaises(IntegrityError):
            res_models.Review.objects.create(resource=self.resource,
                                             author=self.user2,
                                             contents='its nice2',
                                             mark=3)


class TestResource(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='admin',
                                                         password='admin',
                                                         email='admin@admin.com')
        self.user2 = get_user_model().objects.create_user(username='admin2',
                                                          password='admin2',
                                                          email='admin2@admin.com')
        self.resource = res_models.Resource.objects.create(
            name='Tango with Django',
            url='http://www.tangowithdjango.com/',
            description='Cool django book',
            added_by=self.user)

    def test_add_review(self):
        self.resource.add_review(self.user, 'asdfsadf', 5)
        self.assertEqual(self.resource.reviews.count(), 1)


class TestResourceTag(TestCase):
    def setUp(self):
        self.tags = []
        for c in 'abcdefghijk':
            self.tags.append(res_models.ResourceTag.objects.create(name=c))

    def test_get_tags_grid(self):
        tags = res_models.ResourceTag.objects.order_by('name')
        expected = [
            [t for t in self.tags[0:6]],
            [t for t in self.tags[6:]],
        ]
        print(expected)
        result = res_models.ResourceTag.get_tags_grid(self.tags, 6)
        print(result)
        self.assertEqual(expected, result)
