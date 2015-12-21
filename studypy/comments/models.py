from django.db import models
from django.conf import settings

from utils.models import Timestampable


class ResourceComment(Timestampable, models.Model):
    resource = models.ForeignKey('resources.Resource', verbose_name='resource',
                                 related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='author')
    contents = models.CharField('contents', max_length=1000)

    class Meta:
        ordering = ['-created_at']
