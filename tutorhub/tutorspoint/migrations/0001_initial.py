# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'First Name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Last Name', blank=True)),
                ('qual', models.CharField(max_length=30, verbose_name=b'Qualification', blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name=b'Phone Number', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'First Name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Last Name', blank=True)),
                ('qual', models.CharField(max_length=30, verbose_name=b'Qualification', blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name=b'Phone Number', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
