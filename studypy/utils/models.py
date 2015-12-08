from django.db import models


class Timestampable(models.Model):
    created_at = models.DateTimeField('created at', auto_now_add=True)
    modified_at = models.DateTimeField('modified at', auto_now=True)

    class Meta:
        abstract = True
