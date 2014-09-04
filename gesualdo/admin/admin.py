from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from gesualdo.models.location import Location
from gesualdo.models.library import Library
from gesualdo.models.role import Role
from gesualdo.models.person import Person

from gesualdo.models.book import Book
"""from gesualdo.models.genre_musical_normalise import GenreMusicalNormalise
from gesualdo.models.genre_musical_detaille import GenreMusicalDetaille"""
from gesualdo.models.book_copy import BookCopy
from gesualdo.models.catalog import Catalog
from gesualdo.models.piece import Piece
"""from gesualdo.models.file import File"""
from gesualdo.models.message import Message
from gesualdo.models.userprofile import UserProfile
from gesualdo.models.text import Text

def reindex_in_solr(modeladmin, request, queryset):
    # calls the save method on every item, ensuring the
    # post_save handler is called
    for item in queryset:
        print(item)
        item.save()
    reindex_in_solr.short_description = "Re-Index Selected Items"



class LocationAdmin(admin.ModelAdmin):
    ordering = ('standardized_country', 'standardized_city')

class LibraryAdmin(admin.ModelAdmin):
    ordering = ('rism_siglum',)

class RoleAdmin(admin.ModelAdmin):
    pass

class PersonAdmin(admin.ModelAdmin):
    filter_horizontal=('workplace', 'role', )
    ordering = ('surname',)

class TextAdmin(admin.ModelAdmin):
    pass
    actions = [reindex_in_solr]  

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'rism', 'date',)
    filter_horizontal=('composers', 'catalog_id', 'copyists', 'other_editions')
    actions = [reindex_in_solr]    

"""class FilePieceInline(admin.TabularInline):
    model = Piece.fichiers_joints.through
    can_delete = True,
    verbose_name = "File"
    verbose_name_plural = "Files" """

class PieceAdmin(admin.ModelAdmin):
    list_display = ('title', 'book_position', 'maincopy', 'composer')
    ordering = ('title',)
    actions = [reindex_in_solr]
    """inlines = (
        FilePieceInline,
    )"""
    actions = [reindex_in_solr]

class GenreMusicalNormaliseAdmin(admin.ModelAdmin):
    pass

class GenreMusicalDetailleAdmin(admin.ModelAdmin):
    pass

class BookCopyAdmin(admin.ModelAdmin):
    search_fields = ('shelfmark', 'book_id__title')
    list_display = ('shelfmark', 'location', 'book_id')
    actions = [reindex_in_solr]

class CatalogAdmin(admin.ModelAdmin):
    search_fields =('identifier',)
    list_display = ('choice_catalog', 'identifier')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'piece','validated', 'archived')

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (
        UserInline,
    )

admin.site.register(Location, LocationAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Book, BookAdmin)
"""admin.site.register(GenreMusicalNormalise, GenreMusicalNormaliseAdmin)
admin.site.register(GenreMusicalDetaille, GenreMusicalDetailleAdmin)"""
admin.site.register(BookCopy, BookCopyAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Piece, PieceAdmin)
"""admin.site.register(File)"""
admin.site.register(Message, MessageAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Text, TextAdmin)
