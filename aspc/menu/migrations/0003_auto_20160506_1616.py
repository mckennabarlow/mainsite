# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-06 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]
