# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0007_post_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redditor',
            name='is_gold',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='redditor',
            name='is_mod',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
