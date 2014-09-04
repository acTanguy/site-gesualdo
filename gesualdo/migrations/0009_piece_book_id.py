# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gesualdo', '0008_auto_20140904_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='book_id',
            field=models.ForeignKey(related_name=b'include', to_field=b'book_id', blank=True, to='gesualdo.Book', null=True),
            preserve_default=True,
        ),
    ]
