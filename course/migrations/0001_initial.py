# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('available_from', models.DateField()),
                ('available_to', models.DateField(null=True)),
                ('status', models.CharField(max_length=1, default='a')),
            ],
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('credit', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=1, default='a')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('status', models.CharField(max_length=1, default='a')),
                ('course', models.ForeignKey(to='course.Course')),
            ],
        ),
    ]
