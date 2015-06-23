# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0002_auto_20150622_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_user',
            new_name='comment_by_user',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_made',
            field=models.TextField(blank=True),
        ),
    ]
