# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='No description'),
        ),
    ]
