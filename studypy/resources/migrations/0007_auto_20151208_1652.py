# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20151208_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at', default=datetime.datetime(2015, 12, 8, 16, 52, 39, 563488, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='modified_at',
            field=models.DateTimeField(verbose_name='modified at', auto_now=True, default=datetime.datetime(2015, 12, 8, 16, 52, 44, 98530, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
