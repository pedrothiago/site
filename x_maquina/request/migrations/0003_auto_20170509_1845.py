# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20170509_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='sent_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Enviado em'),
        ),
    ]
