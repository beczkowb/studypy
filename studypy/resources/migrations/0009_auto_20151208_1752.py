# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_auto_20151208_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='name'),
        ),
    ]
