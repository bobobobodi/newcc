# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-01 09:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0012_auto_20180331_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transuser',
            name='money',
        ),
        migrations.RemoveField(
            model_name='transuser',
            name='name_tarif',
        ),
    ]