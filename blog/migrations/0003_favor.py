# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150304_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like', models.IntegerField(default=0)),
                ('article', models.ForeignKey(to='blog.BlogsPost')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
