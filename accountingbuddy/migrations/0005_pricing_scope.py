# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-06 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountingbuddy', '0004_pricing_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='scope',
            field=models.CharField(default='Professional', help_text='E.G Profesionals , Companies, Etc', max_length=200, verbose_name='Enter Customer Scope'),
            preserve_default=False,
        ),
    ]
