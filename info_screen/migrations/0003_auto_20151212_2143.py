# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_screen', '0002_auto_20151025_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoscreen',
            name='back_link',
        ),
        migrations.RemoveField(
            model_name='infoscreen',
            name='owners',
        ),
        migrations.DeleteModel(
            name='BackLink',
        ),
    ]
