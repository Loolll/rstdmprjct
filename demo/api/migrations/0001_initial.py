# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-03 13:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='rock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.CharField(db_index=True, max_length=64, verbose_name='vid')),
                ('color', models.CharField(max_length=64, verbose_name='Color')),
                ('rcktp', models.CharField(default='Unknown', max_length=64, verbose_name='Type')),
                ('size', models.IntegerField(choices=[(1, 'big'), (2, 'small'), (3, 'middle'), (4, 'unique')], max_length=64, verbose_name='Size')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
