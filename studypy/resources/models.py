from django.db import models
from django.conf import settings

from utils.models import Timestampable

MARK_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Resource(Timestampable, models.Model):
    name = models.CharField('name', unique=True, max_length=100)
    url = models.URLField('resource url', blank=True)
    description = models.CharField('description', max_length=2000)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField('ResourceTag', verbose_name='tags')


class Review(models.Model):
    resource = models.ForeignKey('Resource', verbose_name='resource')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='author')
    contents = models.TextField('contents')
    mark = models.PositiveIntegerField('mark', choices=MARK_CHOICES)


class ResourceTag(models.Model):
    name = models.CharField('name', max_length=50, unique=True)