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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='name')),
                ('url', models.URLField(blank=True, verbose_name='resource url')),
                ('description', models.CharField(verbose_name='description', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('contents', models.TextField(verbose_name='contents')),
            ],
        ),
    ]
