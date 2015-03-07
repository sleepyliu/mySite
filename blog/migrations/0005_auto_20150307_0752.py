# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150306_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogspost',
            name='title',
            field=models.TextField(max_length=150),
            preserve_default=True,
        ),
    ]
