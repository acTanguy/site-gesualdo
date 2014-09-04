# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gesualdo', '0007_auto_20140903_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='mesure',
            new_name='measure',
        ),
    ]
