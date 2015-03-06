# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_favor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favor',
            name='article',
        ),
        migrations.DeleteModel(
            name='Favor',
        ),
        migrations.AddField(
            model_name='blogspost',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
