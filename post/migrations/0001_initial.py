# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content', models.TextField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('status', models.CharField(max_length=1, default='a')),
                ('course', models.ForeignKey(to='course.Course')),
                ('creator', models.ForeignKey(to='member.Member')),
                ('response_to', models.ForeignKey(null=True, to='post.Post')),
            ],
        ),
    ]
