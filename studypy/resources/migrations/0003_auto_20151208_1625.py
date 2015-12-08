# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20151208_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='tags',
            field=models.ManyToManyField(verbose_name='tags', to='resources.ResourceTag'),
        ),
    ]
