# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('info_screen', '0004_auto_20151212_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoscreen',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True),
        ),
    ]
