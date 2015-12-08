# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(verbose_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='resource',
            field=models.ForeignKey(verbose_name='resource', to='resources.Resource'),
        ),
        migrations.AddField(
            model_name='resource',
            name='added_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
