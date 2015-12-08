# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0009_auto_20151208_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='rating',
            field=models.DecimalField(decimal_places=4, verbose_name='rating', max_digits=5, default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.PositiveIntegerField(verbose_name='mark', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
