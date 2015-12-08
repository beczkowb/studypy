from django.db import models
from django.conf import settings

from utils.models import Timestampable

MARK_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Resource(Timestampable, models.Model):
    name = models.CharField('name', unique=True, max_length=50)
    url = models.URLField('resource url', unique=True)
    description = models.CharField('description', max_length=2000)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField('ResourceTag', verbose_name='tags')
    rating = models.DecimalField('rating', max_digits=5, decimal_places=4,
                                 default=0)

    def __str__(self):
        return self.name


class Review(Timestampable, models.Model):
    resource = models.ForeignKey('Resource', verbose_name='resource')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='author')
    contents = models.TextField('contents')
    mark = models.PositiveIntegerField('mark', choices=MARK_CHOICES)

    class Meta:
        unique_together = (('resource', 'author'),)

    def __str__(self):
        return '{resource}=>{author}({mark})'.format(resource=self.resource,
                                                     author=self.author,
                                                     mark=self.mark)

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        number_of_reviews = Review.objects.count()
        marks_sum = Review.objects.filter(
            resource=self.resource).aggregate(models.Sum('mark'))
        self.resource.rating = marks_sum / number_of_reviews
        self.resource.save()


class ResourceTag(models.Model):
    name = models.CharField('name', max_length=50, unique=True)

    def __str__(self):
        return self.name