from rest_framework import serializers
from news.models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validate_data):
        print(validate_data)
        return Article.objects.create(**validate_data)

    def update(self, intance, validated_data):
        intance.author = validated_data.get('author', intance.author)
        intance.title = validated_data.get('title', intance.title)
        intance.description = validated_data.get(
            'description', intance.description
        )
        intance.body = validated_data.get('body', intance.body)
        intance.location = validated_data.get('location', intance.location)
        intance.publication_date = validated_data.get(
            'publication_date', intance.publication_date
        )
        intance.active = validated_data.get('active', intance.active)
        intance.save()
        return intance
    