# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-06 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountingbuddy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='region',
            field=models.CharField(choices=[('USA', 'USA'), ('GULF', 'GULF'), ('ASIA', 'ASIA'), ('EUROPE', 'EUROPE')], default=2, help_text='Select your Region', max_length=200, verbose_name='Select Region'),
            preserve_default=False,
        ),
    ]
