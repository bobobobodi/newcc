# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0009_transuser_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transuser',
            name='money',
            field=models.CharField(default='100', max_length=200),
        ),
    ]
