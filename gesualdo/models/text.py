from django.db import models
from gesualdo.helpers.slugify import unique_slugify
from gesualdo.helpers.slugify import unique_itemify
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save, m2m_changed


class Text(models.Model):
    class Meta:
        app_label="gesualdo"

    item = models.SlugField(blank=True, null=True)

    literary_title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=255, blank=True, null=True)
    translate_title_EN = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey('gesualdo.Person', related_name='Author_of', blank=True, null=True)
    book = models.CharField(max_length=255, blank=True, null=True)
    literary_form = models.CharField(max_length=255, blank=True, null=True)
    rhymes = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    source = models.URLField(max_length=200,blank=True, null=True)

    def save(self, **kwargs):
        item_str = "%s" % (self.literary_title)
        unique_itemify(self, item_str)
        super(Text, self).save()

    def __unicode__(self):
        return u"{0}".format(self.literary_title)

"""@receiver(post_save, sender=Texte)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:gesualdo_texte item:{0}".format(instance.id), q_op="AND")
    if record:
        solrconn.delete(record.results[0]['id'])

    texte = instance
    d = {
        'type':'gesualdo_texte',
        'id':str(uuid.uuid4()),
        'slug':texte.slug, 
        'titre':texte.titre,
        'auteur':texte.auteur,


    }
    solrconn.add(**d)
    solrconn.commit()

@receiver(post_delete, sender=Texte)
def solr_delete(sender, instance, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:gesualdo_texte item:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove it first.
        solrconn.delete(record.results[0]['id'])"""

