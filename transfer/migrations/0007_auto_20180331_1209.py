# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 07:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0006_transuser_year_in_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transuser',
            old_name='year_in_school',
            new_name='name_tarif',
        ),
    ]
