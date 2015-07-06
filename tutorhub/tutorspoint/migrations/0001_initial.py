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
            name='Base_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.CharField(max_length=30, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='First_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name', blank=True)),
                ('age', models.IntegerField(verbose_name=b'Age')),
                ('sex', models.CharField(max_length=10, verbose_name=b'Sex', blank=True)),
                ('address1', models.CharField(max_length=100, verbose_name=b'Address Line 1', blank=True)),
                ('address2', models.CharField(max_length=100, verbose_name=b'Address Line 2', blank=True)),
                ('zipcode', models.CharField(max_length=6, verbose_name=b'ZIP code', blank=True)),
                ('city', models.CharField(max_length=100, verbose_name=b'City', blank=True)),
                ('state', models.CharField(max_length=100, verbose_name=b'State', blank=True)),
                ('country', models.CharField(max_length=100, verbose_name=b'Country', blank=True)),
                ('qual', models.CharField(max_length=100, verbose_name=b'Qualification', blank=True)),
                ('phone_number', models.CharField(max_length=15, verbose_name=b'Phone Number', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('skills', models.CharField(max_length=100, blank=True)),
                ('mode', models.CharField(max_length=100, blank=True)),
                ('location', models.CharField(max_length=100, verbose_name=b'Preferred Locations', blank=True)),
                ('classes', models.CharField(max_length=100, verbose_name=b'Preferred Classes', blank=True)),
                ('subjects', models.CharField(max_length=100, verbose_name=b'Preferred Subjects', blank=True)),
                ('exp', models.CharField(max_length=30, verbose_name=b'Teaching Experience', blank=True)),
                ('lfee', models.IntegerField(default=-1)),
                ('hfee', models.IntegerField(default=-1)),
                ('pic', models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Second_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'First Name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Last Name', blank=True)),
                ('qual', models.CharField(max_length=30, verbose_name=b'Qualification', blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name=b'Phone Number', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
