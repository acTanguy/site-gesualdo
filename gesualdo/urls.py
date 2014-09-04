from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

from gesualdo.views.search import SearchView
from gesualdo.views.auth import LogoutView
from gesualdo.views.auth import LoginFormView

urlpatterns = patterns('',
    # Examples:
    url(r'^gesualdo/$', 'gesualdo.views.main.home', name='home'),
    # url(r'^gesualdo/blog/', include('blog.urls')),
    url(r'^gesualdo/books/$', 'gesualdo.views.main.books', name='books'),
    url(r'^gesualdo/pieces/$', 'gesualdo.views.main.pieces', name='pieces'),
    url(r'^gesualdo/browse/(?P<pk>\w+)$', 'gesualdo.views.main.book', name='book'),
    url(r'^gesualdo/browse/(?P<book>\w+)/(?P<place>\w+)$', 'gesualdo.views.main.piece', name='piece'),

    
    url(r'^gesualdo/admin/', include(admin.site.urls)),
    url(r'^gesualdo/participants/$', 'gesualdo.views.main.participants', name='participants'), 
    url(r'^gesualdo/messageprocessing/', include('gesualdo.urlsMessageprocessing', namespace='messageprocessing')),
    url(r'^gesualdo/login/', LoginFormView.as_view(), name="login-view"),
    url(r'^gesualdo/logout/', LogoutView.as_view(), name="logout-view"),
    url(r'^gesualdo/search/$', SearchView.as_view(), name="search-view"),
    url(r'^gesualdo/lyricists/$', 'gesualdo.views.main.lyricists', name='lyricists'),
    url(r'^gesualdo/lyricist/(?P<pk>[\w\-]+)$', 'gesualdo.views.main.lyricist', name='lyricist'),
)

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^gesualdo/gesualdo/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}), url(r'^gesualdo/gesualdo/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,})) 
    """url(r'^gesualdo/texts/$', 'gesualdo.views.main.textes', name='texts'),
    url(r'^gesualdo/text/(?P<pk>[\w\-]+)$', 'gesualdo.views.main.texte', name='text'),"""