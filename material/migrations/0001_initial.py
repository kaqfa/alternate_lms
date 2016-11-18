# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('filename', models.FileField(upload_to='uploads/material', null=True)),
                ('url', models.CharField(null=True, max_length=255)),
                ('text', models.TextField(null=True)),
                ('type', models.CharField(max_length=1)),
                ('status', models.CharField(max_length=1, default='a')),
                ('content', models.ForeignKey(to='course.Content')),
            ],
        ),
    ]
