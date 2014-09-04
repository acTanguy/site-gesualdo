from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from gesualdo.helpers.slugify import unique_itemify

class Book(models.Model):
    class Meta:
        app_label = "gesualdo"


    PRINT = 'print'
    MANUSCRIT = 'manuscript'
    FORMAT = (
        (MANUSCRIT, 'manuscrit'),
        (PRINT, 'print'),
    )

    item = models.SlugField(db_index=True, blank=True, unique=True, null=True)
    book_id = models.CharField(max_length=255, unique=True, blank=True, null=True)

    complete_title = models.CharField(max_length=255, blank=True, null=True)
    fr_transcribed_complete_title = models.CharField(max_length=255, blank=True, null=True)
    en_transcribed_complete_title = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    fr_transcribed_title = models.CharField(max_length=255, blank=True, null=True)
    en_transcribed_title = models.CharField(max_length=255, blank=True, null=True)

    catalog_id = models.ManyToManyField('gesualdo.Catalog', blank=True, null=True)
    support = models.CharField(max_length=9, choices=FORMAT, default=PRINT)
    place_publication = models.ForeignKey('gesualdo.Location', blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)

    publisher = models.ForeignKey('gesualdo.Person', related_name='publish_by', blank=True, null=True)
    bookseller = models.ForeignKey('gesualdo.Person', related_name='sell_by', blank=True, null=True)
    copyists = models.ManyToManyField('gesualdo.Person', related_name='copie_by', blank=True, null=True)
    composers = models.ManyToManyField('gesualdo.Person', related_name='compose_by', blank=True, null=True)

    number_pieces = models.IntegerField(max_length=4, blank=True, null=True)
    """genre_musical_normalise = models.ManyToManyField('gesualdo.GenreMusicalNormalise', blank=True, null=True)
    genre_musical_detaille = models.ManyToManyField('gesualdo.GenreMusicalDetaille', blank=True, null=True)"""
    other_editions = models.ManyToManyField("self", blank=True, null=True)
    
    notes = models.TextField(blank=True, null=True)

    def save(self, **kwargs):
        item_str = "%s" % (self.book_id)
        unique_itemify(self, item_str)
        super(Book, self).save()

    def rism(self):
        try:
            rism = self.catalog_id.filter(choice_catalog='RISM_A')[0].identifier
        except:
            rism=""
        return rism

    def composer(self):
        composer = ""
        for f in self.composers.all():
            surname = "{0} {1}".format(f.given_name, f.name)
            composer+=surname+', '
        return composers[:-2]

    def __unicode__(self):
        if (self.rism()==""):
            return u"{0}, {1}".format(self.title, self.date)
        else:
            return u"{0}, {1}, {2}".format(self.rism(), self.title, self.date)


"""@receiver(post_save, sender=Recueil)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr
    from gesualdo.models.personne import Personne

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:gesualdo_recueil item:{0}".format(instance.id))
    if record:
        solrconn.delete(record.results[0]['id'])

    recueil = instance
    nom_compositeurs = []
    for f in recueil.compositeurs.all():
        nom = "{0}, {1}".format(f.nom, f.prenom)
        nom_compositeurs.append(nom)
    d = {
        'type':'gesualdo_recueil',
        'id':str(uuid.uuid4()),
        'item':recueil.item,
        'recueil_id':recueil.recueil_id,
        
        
        
        'nom_compositeurs':nom_compositeurs,
        


        

    }
    solrconn.add(**d)
    solrconn.commit()
'''
@receiver(post_delete, sender=Recueil)
def solr_delete(sender, instance, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:gesualdo_recueil item:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove it first.
        solrconn.delete(record.results[0]['id'])"""
