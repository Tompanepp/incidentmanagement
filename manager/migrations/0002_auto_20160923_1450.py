# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 14:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintanancerequest',
            name='expirationdate',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 30, 14, 50, 57, 646407)),
        ),
    ]