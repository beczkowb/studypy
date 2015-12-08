from django.db import models
from django.conf import settings


class Resource(models.Model):
    name = models.CharField('name', unique=True, max_length=100)
    url = models.URLField('resource url', blank=True)
    description = models.CharField('description', max_length=2000)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL)


class Review(models.Model):
    resource = models.ForeignKey('Resource', verbose_name='resource')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='author')
    contents = models.TextField('contents')
