# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 16:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20160925_2103'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MaintenanceType',
            new_name='UserType',
        ),
        migrations.RemoveField(
            model_name='maintainer',
            name='type',
        ),
        migrations.RemoveField(
            model_name='maintanancerequest',
            name='maintainerId',
        ),
        migrations.AddField(
            model_name='profile',
            name='usertype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.UserType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maintanancerequest',
            name='expirationdate',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 7, 16, 41, 49, 464694)),
        ),
        migrations.AlterField(
            model_name='maintanancerequest',
            name='residence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.Residence'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='residence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.Residence'),
        ),
        migrations.DeleteModel(
            name='Maintainer',
        ),
        migrations.DeleteModel(
            name='MaintainerType',
        ),
    ]
