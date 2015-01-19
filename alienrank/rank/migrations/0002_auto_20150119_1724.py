# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to='rank.Redditor', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='subreddit',
            field=models.ForeignKey(to='rank.Subreddit', null=True),
            preserve_default=True,
        ),
    ]
