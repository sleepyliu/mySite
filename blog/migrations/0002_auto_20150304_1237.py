# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogspost',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='timestamp',
            field=models.DateTimeField(verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
