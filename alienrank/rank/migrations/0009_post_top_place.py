# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0008_auto_20150120_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='top_place',
            field=models.IntegerField(null=True, db_index=True),
            preserve_default=True,
        ),
    ]
