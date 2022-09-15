from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    # Serialize the books

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn','author')

class AuthorSerializer(serializers.ModelSerializer):
    # Serializing all the Authors
    books = BookSerializer(read_only=True, many=True, source="book_set")

    class Meta:
        model = Author
        fields = ('id','first_name','last_name','books')


