from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^addCom$', 'gesualdo.views.messageprocessing.addComment', name='addComment'),
    url(r'^remCom$', 'gesualdo.views.messageprocessing.refuseComment', name='refuseComment'),
    url(r'^validateCom$', 'gesualdo.views.messageprocessing.validateComment', name='validateComment'),
    url(r'^archiveCom', 'gesualdo.views.messageprocessing.archiveComment', name='archiveComment'),
)