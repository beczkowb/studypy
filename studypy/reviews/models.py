from django.db import models
from django.conf import settings

from utils.models import Timestampable


class Review(Timestampable, models.Model):
    MARK_CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    resource = models.ForeignKey('resources.Resource', verbose_name='resource',
                                 related_name='reviews')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='author')
    contents = models.TextField('contents', blank=True)
    mark = models.PositiveIntegerField('mark', choices=MARK_CHOICES)

    class Meta:
        unique_together = (('resource', 'author'),)

    @property
    def number_of_comments(self):
        return self.comments.all().count()

    def __str__(self):
        return '{resource}=>{author}({mark})'.format(resource=self.resource,
                                                     author=self.author,
                                                     mark=self.mark)