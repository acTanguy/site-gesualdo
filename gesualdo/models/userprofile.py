from django.db import models
from django.contrib.auth.models import User

from gesualdo.models.person import Person

class UserProfile(models.Model):
    class Meta:
        app_label = "gesualdo"

    user = models.OneToOneField(User, db_index=True, parent_link="pseudo")
    person = models.ForeignKey(Person, blank=True, null=True, help_text="Link this account with a DuChemin User", db_index=True, related_name="profile")
    def __unicode__(self):
        return self.personne.nom_bref

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
