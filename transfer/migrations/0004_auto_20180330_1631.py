# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0003_auto_20180330_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transuser',
            name='money_on',
            field=models.IntegerField(),
        ),
    ]