from django.db import models


class Resource(models.Model):
    name = models.CharField('name', unique=True)
    url = models.URLField('resource url', blank=True)
    description = models.CharField('description')


class Review(models.Model):
    resource = models.ForeignKey('Resource', verbose_name='resource')