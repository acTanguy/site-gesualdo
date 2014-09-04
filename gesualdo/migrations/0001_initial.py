# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.SlugField(unique=True, null=True, blank=True)),
                ('book_id', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('complete_title', models.CharField(max_length=255, null=True, blank=True)),
                ('fr_transcribed_complete_title', models.CharField(max_length=255, null=True, blank=True)),
                ('en_transcribed_complete_title', models.CharField(max_length=255, null=True, blank=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('fr_transcribed_title', models.CharField(max_length=255, null=True, blank=True)),
                ('en_transcribed_title', models.CharField(max_length=255, null=True, blank=True)),
                ('support', models.CharField(default=b'print', max_length=9, choices=[(b'manuscript', b'manuscrit'), (b'print', b'print')])),
                ('date', models.CharField(max_length=255, null=True, blank=True)),
                ('number_pieces', models.IntegerField(max_length=4, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.SlugField(unique=True, null=True, blank=True)),
                ('shelfmark', models.CharField(max_length=16, null=True, blank=True)),
                ('state', models.CharField(default=b'COMPLETE', max_length=9, choices=[(b'COMPLETE', b'Complete'), (b'INCOMPLETE', b'Incomplete')])),
                ('preservation', models.CharField(default=b'Preserved', max_length=9, choices=[(b'Preserved', b'Preserved'), (b'LACKING', b'Lacking')])),
                ('book_copy_notes', models.TextField(null=True, blank=True)),
                ('book_copy_link', models.URLField(null=True, blank=True)),
                ('voice_name', models.CharField(max_length=255, null=True, blank=True)),
                ('component_preserved', models.CharField(max_length=255, null=True, blank=True)),
                ('component_lacking', models.CharField(max_length=255, null=True, blank=True)),
                ('voice_notes', models.TextField(null=True, blank=True)),
                ('book_id', models.ForeignKey(related_name=b'locate', to_field=b'book_id', blank=True, to='gesualdo.Book', null=True)),
            ],
            options={
                'verbose_name': 'Book Copy',
                'verbose_name_plural': 'Book Copies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_catalog', models.CharField(default=b'RISM_A', max_length=10, choices=[(b'RISM_A', b'Rism A'), (b'RISM_B', b'Rism B'), (b'CENSUS', b'Census'), (b'VOGEL', b'Vogel'), (b'BROWN', b'Brown'), (b'HEARTZ', b'Hearz'), (b'VANHULST', b'Vanhulst'), (b'LESURE', b'Lesure'), (b'POGUE', b'Pogue'), (b'AGEE', b'Agee'), (b'BERNSTEIN', b'Bernstein'), (b'BOETTICHER', b'Boetticher'), (b'BOORMAN', b'Boorman'), (b'GUILLO', b'Guillo'), (b'LEWIS', b'Lewis'), (b'SARTORI', b'Sartori'), (b'WEAVER', b'Weaver'), (b'PATALAS', b'Patalas'), (b'GOOVEARTS', b'Goovearts')])),
                ('identifier', models.CharField(max_length=32, unique=True, null=True, blank=True)),
                ('n_pdf', models.CharField(max_length=32, null=True, blank=True)),
                ('n_mf', models.CharField(max_length=32, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('standardized_name', models.CharField(max_length=255, null=True, blank=True)),
                ('rism_siglum', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Library',
                'verbose_name_plural': 'Libraries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('standardized_country', models.CharField(max_length=255)),
                ('french_country', models.CharField(max_length=255, null=True, blank=True)),
                ('standardized_city', models.CharField(max_length=255, null=True, blank=True)),
                ('french_city', models.CharField(max_length=255, null=True, blank=True)),
                ('place_name', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('voice', models.CharField(max_length=10, null=True, blank=True)),
                ('mesure', models.SmallIntegerField()),
                ('validated', models.BooleanField(default=False)),
                ('archive', models.BooleanField(default=False)),
                ('ip', models.GenericIPAddressField()),
                ('file_to_upload', models.FileField(null=True, upload_to=b'user_file')),
            ],
            options={
                'permissions': (('validate_message', 'Can validate messages'), ('archive_message', 'Can archive messages')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surname', models.CharField(max_length=255, null=True, blank=True)),
                ('given_name', models.CharField(max_length=255, null=True, blank=True)),
                ('variant_nom', models.CharField(max_length=255, null=True, blank=True)),
                ('nickname', models.CharField(max_length=255, null=True, blank=True)),
                ('active_period', models.CharField(max_length=16, null=True, blank=True)),
                ('bibliography', models.TextField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('birth_place', models.ForeignKey(related_name=b'birth_place_of', blank=True, to='gesualdo.Location', null=True)),
                ('death_place', models.ForeignKey(related_name=b'death_place_of', blank=True, to='gesualdo.Location', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.SlugField(unique=True, null=True, blank=True)),
                ('title', models.CharField(max_length=255)),
                ('book_position', models.CharField(max_length=4, null=True, blank=True)),
                ('voices_number', models.IntegerField(max_length=4, null=True, blank=True)),
                ('voices_name', models.CharField(max_length=256, null=True, blank=True)),
                ('pdf_link', models.URLField(null=True, blank=True)),
                ('mei_link', models.FileField(upload_to=b'partitions')),
                ('mp3_link', models.URLField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('composer', models.ForeignKey(related_name=b'composition', blank=True, to='gesualdo.Person', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.SlugField(null=True, blank=True)),
                ('literary_title', models.CharField(max_length=255)),
                ('short_title', models.CharField(max_length=255, null=True, blank=True)),
                ('translate_title_EN', models.CharField(max_length=255, null=True, blank=True)),
                ('book', models.CharField(max_length=255, null=True, blank=True)),
                ('literary_form', models.CharField(max_length=255, null=True, blank=True)),
                ('rhymes', models.CharField(max_length=255, null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('source', models.URLField(null=True, blank=True)),
                ('author', models.ForeignKey(related_name=b'Author_of', blank=True, to='gesualdo.Person', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person', models.ForeignKey(related_name=b'profile', blank=True, to='gesualdo.Person', help_text=b'Link this account with a DuChemin User', null=True)),
                ('user', models.OneToOneField(parent_link=b'pseudo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='piece',
            name='lyrics',
            field=models.ForeignKey(related_name=b'text_of', blank=True, to='gesualdo.Text', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='mainsource',
            field=models.ForeignKey(related_name=b'piece_of', to_field=b'item', blank=True, to='gesualdo.BookCopy', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='othersources',
            field=models.ManyToManyField(related_name=b'piece_in', null=True, to='gesualdo.BookCopy', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='poet_lyricist',
            field=models.ForeignKey(related_name=b'works', blank=True, to='gesualdo.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ManyToManyField(related_name=b'role_of', null=True, to='gesualdo.Role', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='workplace',
            field=models.ManyToManyField(related_name=b'active_place_of', null=True, to='gesualdo.Location', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='piece',
            field=models.ForeignKey(to='gesualdo.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='user_post',
            field=models.ForeignKey(blank=True, to='gesualdo.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='library',
            name='location',
            field=models.ForeignKey(to='gesualdo.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookcopy',
            name='location',
            field=models.ForeignKey(blank=True, to='gesualdo.Library', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='bookseller',
            field=models.ForeignKey(related_name=b'sell_by', blank=True, to='gesualdo.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='catalog_id',
            field=models.ManyToManyField(to='gesualdo.Catalog', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='composers',
            field=models.ManyToManyField(related_name=b'compose_by', null=True, to='gesualdo.Person', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='copyists',
            field=models.ManyToManyField(related_name=b'copie_by', null=True, to='gesualdo.Person', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='other_editions',
            field=models.ManyToManyField(related_name='other_editions_rel_+', null=True, to='gesualdo.Book', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='place_publication',
            field=models.ForeignKey(blank=True, to='gesualdo.Location', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(related_name=b'publish_by', blank=True, to='gesualdo.Person', null=True),
            preserve_default=True,
        ),
    ]
