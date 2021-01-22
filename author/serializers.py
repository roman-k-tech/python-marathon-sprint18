from rest_framework import serializers
from .models import Author


class AuthorCommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = 'name', 'surname', 'patronymic'
