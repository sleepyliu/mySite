# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150307_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogspost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
