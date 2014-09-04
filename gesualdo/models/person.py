from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Person(models.Model):
    class Meta:
        app_label="gesualdo"

    surname = models.CharField(max_length=255, blank=True, null=True)
    given_name = models.CharField(max_length=255, blank=True, null=True)
    variant_nom = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.CharField(max_length=16, blank=True, null=True)
    birth_place = models.ForeignKey("gesualdo.Location", related_name='birth_place_of', blank=True, null=True)
    death_date = models.CharField(max_length=16, blank=True, null=True)
    death_place  = models.ForeignKey("gesualdo.Location", related_name='death_place_of', blank=True, null=True)
    role = models.ManyToManyField("gesualdo.Role", blank=True, null=True, related_name='role_of')
    workplace = models.ManyToManyField("gesualdo.Location", related_name='active_place_of', blank=True, null=True)
    active_period = models.CharField(max_length=16, blank=True, null=True)

    bibliography = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"{0}, ({1})".format(self.surname, self.given_name)

    def official_name(self):
        return u"{0}, {1}".format(self.surname, self.given_name)

    def name(self):
        return u"{0} {1}".format(self.given_name, self.surname)