# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0005_auto_20150120_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subreddit_uid',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
