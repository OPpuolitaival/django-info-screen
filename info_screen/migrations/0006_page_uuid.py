# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('info_screen', '0005_infoscreen_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True),
        ),
    ]
