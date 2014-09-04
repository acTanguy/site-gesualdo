from django.db import models

class Location(models.Model):
    class Meta:
        app_label="gesualdo"

    standardized_country = models.CharField(max_length=255)
    french_country = models.CharField(max_length=255, blank=True, null=True)
    standardized_city = models.CharField(max_length=255, blank=True, null=True)
    french_city = models.CharField(max_length=255, blank=True, null=True)
    place_name  = models.CharField(max_length=255, blank=True, null=True)
    
    def __unicode__(self):
        if self.standardized_city:
            return u"{0}, ({1})".format(self.standardized_country, self.standardized_city)
        else:
            return u"{0}".format(self.standardized_country)
    
    def city(self):
        if self.standardized_city:
            return u"{0}".format(self.standardized_city)
        else:
            return u"{0}".format(self.standardized_country)
