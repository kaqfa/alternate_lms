# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='creator',
            field=models.ForeignKey(to='member.Member'),
        ),
        migrations.AddField(
            model_name='content',
            name='section',
            field=models.ForeignKey(to='course.Section'),
        ),
        migrations.AddField(
            model_name='content',
            name='type',
            field=models.ForeignKey(to='course.ContentType'),
        ),
    ]
