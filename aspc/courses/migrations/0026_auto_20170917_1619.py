# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-17 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0025_auto_20170910_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursereview',
            name='challenge_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coursereview',
            name='respect_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
