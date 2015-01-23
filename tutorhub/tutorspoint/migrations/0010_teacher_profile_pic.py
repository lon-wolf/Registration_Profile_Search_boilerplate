# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorspoint', '0009_auto_20150122_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_profile',
            name='pic',
            field=models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/'),
            preserve_default=True,
        ),
    ]
