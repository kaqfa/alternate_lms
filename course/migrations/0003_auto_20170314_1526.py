# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20161115_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='status',
            field=models.CharField(choices=[('a', 'Aktif'), ('i', 'Tidak Aktif')], default='a', max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('a', 'Aktif'), ('i', 'Tidak Aktif')], default='a', max_length=1),
        ),
        migrations.AlterField(
            model_name='section',
            name='status',
            field=models.CharField(choices=[('a', 'Aktif'), ('i', 'Tidak Aktif')], default='a', max_length=1),
        ),
    ]