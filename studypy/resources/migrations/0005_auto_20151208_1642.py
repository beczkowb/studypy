# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_review_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='created_at',
            field=models.DateTimeField(verbose_name='created at', default=datetime.datetime(2015, 12, 8, 16, 42, 32, 404201, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='modified_at',
            field=models.DateTimeField(verbose_name='modified at', default=datetime.datetime(2015, 12, 8, 16, 42, 38, 814477, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
