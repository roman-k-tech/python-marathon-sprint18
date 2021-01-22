from rest_framework import serializers
from .models import Book


class BookCommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# class BookUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = 'name', 'description', 'count', 'authors'
