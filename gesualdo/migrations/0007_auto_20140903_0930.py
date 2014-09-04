# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gesualdo', '0006_auto_20140902_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='identifier',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='catalog',
            unique_together=set([('choice_catalog', 'identifier')]),
        ),
    ]
