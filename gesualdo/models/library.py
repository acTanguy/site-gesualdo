from django.db import models

class Library(models.Model):
    class Meta:
        app_label="gesualdo"
        verbose_name = "Library"
        verbose_name_plural = "Libraries"

    standardized_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.ForeignKey("gesualdo.Location")
    rism_siglum = models.CharField(max_length=255, blank=True, null=True)


    def __unicode__(self):
        return u"{0} / {1}. {02}".format(self.rism_siglum, self.location, self.standardized_name)