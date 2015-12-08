# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20151208_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='mark',
            field=models.PositiveIntegerField(verbose_name='mark', default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=False,
        ),
    ]
