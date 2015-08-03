# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorspoint', '0002_auto_20150708_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='second_profile',
            name='pic',
            field=models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'/'),
            preserve_default=True,
        ),
    ]
