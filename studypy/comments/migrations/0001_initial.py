# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0002_auto_20151219_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceComment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(verbose_name='created at', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='modified at', auto_now=True)),
                ('contents', models.CharField(max_length=1000, verbose_name='contents')),
                ('author', models.ForeignKey(verbose_name='author', to=settings.AUTH_USER_MODEL)),
                ('resource', models.ForeignKey(verbose_name='resource', to='resources.Resource')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
