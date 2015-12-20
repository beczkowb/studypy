# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20151219_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='contents',
            field=models.TextField(verbose_name='contents', blank=True),
        ),
    ]
