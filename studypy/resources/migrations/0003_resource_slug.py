# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20151219_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
