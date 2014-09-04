# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gesualdo', '0004_auto_20140902_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcopy',
            name='preservation',
            field=models.CharField(default=b'PRESERVED', max_length=9, choices=[(b'PRESERVED', b'Preserved'), (b'LACKING', b'Lacking')]),
        ),
    ]
