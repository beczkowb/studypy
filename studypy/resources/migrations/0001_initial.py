# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('url', models.URLField(unique=True, verbose_name='resource url')),
                ('description', models.CharField(max_length=2000, verbose_name='description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
