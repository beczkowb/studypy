# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0003_auto_20151220_1122'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewComment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('contents', models.CharField(verbose_name='contents', max_length=1000)),
                ('author', models.ForeignKey(verbose_name='author', to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(verbose_name='review', related_name='comments', to='reviews.Review')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='resourcecomment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='resourcecomment',
            name='resource',
            field=models.ForeignKey(verbose_name='resource', related_name='comments', to='resources.Resource'),
        ),
    ]
