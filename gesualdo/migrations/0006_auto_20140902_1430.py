# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gesualdo', '0005_auto_20140902_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcopy',
            name='preservation',
            field=models.CharField(default=b'PRESERVED', max_length=16, choices=[(b'PRESERVED', b'Preserved'), (b'LACKING', b'Lacking')]),
        ),
        migrations.AlterField(
            model_name='bookcopy',
            name='state',
            field=models.CharField(default=b'COMPLETE', max_length=16, choices=[(b'COMPLETE', b'Complete'), (b'INCOMPLETE', b'Incomplete')]),
        ),
    ]
