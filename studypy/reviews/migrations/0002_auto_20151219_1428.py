# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
        ('resources', '0002_auto_20151219_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='review',
            name='resource',
            field=models.ForeignKey(to='resources.Resource', related_name='reviews', verbose_name='resource'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('resource', 'author')]),
        ),
    ]
