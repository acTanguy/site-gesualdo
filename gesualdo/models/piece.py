import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save, m2m_changed

from gesualdo.helpers.slugify import unique_itemify

class Piece(models.Model):
    class Meta:
        app_label="gesualdo"

    item = models.SlugField(db_index=True, blank=True, unique=True, null=True)
    book_id = models.ForeignKey("gesualdo.Book", to_field='book_id', related_name='include', blank=True, null=True)
    mainsource = models.ForeignKey("gesualdo.BookCopy", to_field='item', related_name='piece_of', blank=True, null=True)
    othersources = models.ManyToManyField("gesualdo.BookCopy", related_name='piece_in', blank=True, null=True)
    title = models.CharField(max_length=255)
    book_position = models.CharField(max_length=4, blank=True, null=True)
    composer = models.ForeignKey('gesualdo.Person', related_name='composition', blank=True, null=True)
    poet_lyricist =  models.ForeignKey('gesualdo.Person',related_name='works', blank=True, null=True)
    lyrics = models.ForeignKey('gesualdo.Text', related_name='text_of', blank=True, null=True)
    """concordances_ms = models.ManyToManyField("self", blank=True, null=True)
    concordances_imp = models.ManyToManyField("self", blank=True, null=True)"""
    voices_number = models.IntegerField(max_length=4, blank=True, null=True)
    voices_name = models.CharField(max_length=256, blank=True, null=True)
    """genre_musical_normalise = models.ForeignKey('gesualdo.GenreMusicalNormalise', blank=True, null=True)
    genre_musical_detaille = models.ForeignKey('gesualdo.GenreMusicalDetaille', blank=True, null=True)"""
    pdf_link = models.URLField(max_length=200,blank=True, null=True)
    mei_link = models.FileField(upload_to=os.path.join("partitions"), blank=True, null=True)
    mp3_link = models.URLField(max_length=200,blank=True, null=True)
    """fichiers_joints = models.ManyToManyField('gesualdo.File', blank=True, null=True)"""

    notes = models.TextField(blank=True, null=True)

    def save(self, **kwargs):
        if self.mainsource:
            item_str = "%s/%s" % (self.mainsource)
        elif self.book_id:
            item_str = "%s/%s" % (self.book_id.book_id, self.book_position)
        else:
            item_str = "%s/%s" % (self.title)
        unique_itemify(self, item_str)
        super(Piece, self).save()


    def __unicode__(self):
        return u"{0}".format(self.title)

    def split_voices(self):
        return self.voices_name.split(',')

    def maincopy(self):
        if self.mainsource:
            return self.mainsource

    

"""@receiver(post_save, sender=Piece)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:gesualdo_piece item:{0}".format(instance.id), q_op="AND")
    if record:
        solrconn.delete(record.results[0]['id'])

    piece = instance
    d = {
        'type':'gesualdo_piece',
        'id':str(uuid.uuid4()),
        'item':piece.item,
        'titre':piece.titre,
        'recueil_id':piece.recueil_id,
        'compositeur':piece.compositeur,
        'parolier':piece.poete_parolier,

        
    }
    solrconn.add(**d)
    solrconn.commit()

@receiver(post_delete, sender=Piece)
def solr_delete(sender, instance, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:gesualdo_piece item:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove it first.
        solrconn.delete(record.results[0]['id'])"""

