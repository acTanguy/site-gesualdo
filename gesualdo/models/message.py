from django.db import models
from gesualdo.models.piece import Piece
from gesualdo.models.userprofile import UserProfile
import os

def new_path(path):
    def wrapper(instance, filename):
        extension = filename.split(',')[-1]
        filename = '{}.{}'.format(instance.pk, extension)
        return path.os.join(path, filename)
    return wrapper

class Message(models.Model):
    user_post = models.ForeignKey(UserProfile, null=True, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    piece = models.ForeignKey(Piece)
    voice = models.CharField(max_length=10, null=True, blank=True)
    measure = models.SmallIntegerField()
    validated = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    ip = models.GenericIPAddressField()
    #mail = models.EmailField(max_length=254)
    file_to_upload = models.FileField(null=True, upload_to=os.path.join("user_file"))
    class Meta:
        app_label="gesualdo"
        permissions = (
            ('validate_message', 'Can validate messages'),
            ('archive_message', 'Can archive messages'),
        )
    def __unicode__(self):
        if self.user_post == None:
            return "Visitor {0}...".format(self.message[:25])
        else:
            return "{0} {1}...".format(self.user_post.person.nickname, self.message[:25])
