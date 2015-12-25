import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone

from utils.models import Timestampable
from reviews.models import Review


class Resource(Timestampable, models.Model):
    name = models.CharField('name', unique=True, max_length=50)
    url = models.URLField('resource url', unique=True)
    description = models.CharField('description', max_length=2000)
    tags = models.ManyToManyField('tags.Tag', verbose_name='tags',
                                  related_name='resources')

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

    def add_review(self, author, contents, mark):
        Review.objects.create(resource=self, author=author, mark=mark,
                              contents=contents)

    @classmethod
    def get_hot(cls):
        today = timezone.now()
        delta_month = datetime.timedelta(days=30)
        resources = cls.objects.filter(created_at__gte=(today - delta_month))
        sorted_resources = sorted(resources, key=lambda r: r.hotness,
                                  reverse=True)
        return sorted_resources

    @classmethod
    def get_newest(cls):
        return cls.objects.order_by('-created_at')

    @property
    def hotness(self):
        today = timezone.now()
        d = today - self.created_at
        return (30 - d.days) * self.number_of_reviews

    @property
    def number_of_reviews(self):
        return self.reviews.all().count()

    @property
    def number_of_comments(self):
        return self.comments.all().count()

    @property
    def avg_mark(self):
        avg = self.reviews.all().aggregate(models.Avg('mark'))['mark__avg']
        return avg if avg else 0

    @property
    def get_top_rated(self):
        return None