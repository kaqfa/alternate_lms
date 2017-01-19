# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, parent_link=True, to=settings.AUTH_USER_MODEL, auto_created=True, serialize=False)),
                ('address', models.CharField(null=True, max_length=255)),
                ('phone', models.CharField(null=True, max_length=20)),
                ('type', models.CharField(choices=[('s', 'mahasiswa'), ('l', 'dosen')], max_length=1, default='s')),
                ('status', models.CharField(max_length=1, default='a')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('activity', models.CharField(max_length=255)),
                ('member', models.ForeignKey(to='member.Member')),
            ],
        ),
    ]
