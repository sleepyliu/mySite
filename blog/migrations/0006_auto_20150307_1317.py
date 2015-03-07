# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150307_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogspost',
            name='title',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
