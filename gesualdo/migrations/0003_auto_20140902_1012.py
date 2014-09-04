# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gesualdo', '0002_auto_20140901_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='archive',
            new_name='archived',
        ),
        migrations.AlterField(
            model_name='bookcopy',
            name='book_id',
            field=models.ForeignKey(related_name=b'locate', to='gesualdo.Book', to_field=b'book_id'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='mei_link',
            field=models.FileField(null=True, upload_to=b'partitions', blank=True),
        ),
    ]
