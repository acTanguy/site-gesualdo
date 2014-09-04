from gesualdo.models.book import Book
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedSerializer):
    class Meta:
        model = Book