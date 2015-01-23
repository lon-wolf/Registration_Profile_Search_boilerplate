# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tutorspoint', '0004_auto_20150114_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='teacher_profile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='address1',
            field=models.CharField(default=' ', max_length=100, verbose_name=b'Address Line 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='address2',
            field=models.CharField(default=' ', max_length=100, verbose_name=b'Address Line 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='age',
            field=models.IntegerField(default=0, verbose_name=b'Age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='city',
            field=models.CharField(default=' ', max_length=100, verbose_name=b'City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='country',
            field=models.CharField(default=' ', max_length=100, verbose_name=b'Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='name',
            field=models.CharField(default=' ', max_length=50, verbose_name=b'Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='sex',
            field=models.CharField(max_length=10, verbose_name=b'Sex', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='state',
            field=models.CharField(default=' ', max_length=100, verbose_name=b'State'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='zipcode',
            field=models.CharField(default=0, max_length=6, verbose_name=b'ZIP code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name=b'Phone Number', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
            preserve_default=True,
        ),
    ]
