from django.db import models

from gesualdo.helpers.slugify import unique_itemify

class BookCopy(models.Model):
    class Meta:
        app_label="gesualdo"
        verbose_name = "Book Copy"
        verbose_name_plural = "Book Copies"

    PRESERVED = "PRESERVED"
    LACKING = "LACKING"
    COMPLETE = 'COMPLETE'
    INCOMPLETE = 'INCOMPLETE'
    STATE =(
        (COMPLETE, 'Complete'),
        (INCOMPLETE, 'Incomplete'),
    )
    PRESERVATION = (
        (PRESERVED, 'Preserved'),
        (LACKING, 'Lacking'),
    )

    item = models.SlugField(db_index=True, blank=True, unique=True, null=True)

    location = models.ForeignKey('gesualdo.Library', blank=True, null=True)
    book_id = models.ForeignKey("gesualdo.Book", to_field='book_id', related_name='locate')
    shelfmark = models.CharField(max_length=16, blank=True, null=True)
    state = models.CharField(max_length=16, choices=STATE, default=COMPLETE)
    preservation = models.CharField(max_length=16, choices=PRESERVATION, default=PRESERVED)
    book_copy_notes = models.TextField(blank=True, null=True)
    book_copy_link = models.URLField(max_length=200,blank=True, null=True)

    voice_name =models.CharField(max_length=255, blank=True, null=True)
    component_preserved = models.CharField(max_length=255, blank=True, null=True)
    component_lacking =models.CharField(max_length=255, blank=True, null=True)

    voice_notes =models.TextField(blank=True, null=True)

    def save(self, **kwargs):
        item_str = "%s/%s" % (self.book_id.book_id, self.location)
        unique_itemify(self, item_str)
        super(BookCopy, self).save()

    def __unicode__(self):
        return u"{0}".format(self.shelfmark)

