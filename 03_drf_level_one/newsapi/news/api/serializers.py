from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist


# class JournalistSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Journalist
#         fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = JournalistSerializer()
    # author = serializers.StringRelatedField()

    class Meta:
        model = Article
        exclude = ('id',)
        # fields = '__all__'
        # fields = ('title', 'description', 'body',)

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta
    
    def validate(self, data):
        '''Check if title and description are the same'''
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                'Title and Description must be differents!'
            )
        return data

    def validate_title(self, value):
        if len(value) < 30:
            raise serializers.ValidationError(
                'The Title has to be at least 30 chars long!'
            )
        return value


class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='article-detail'
    )
    # articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = '__all__'



# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
    
#     def create(self, validate_data):
#         print(validate_data)
#         return Article.objects.create(**validate_data)

#     def update(self, intance, validated_data):
#         intance.author = validated_data.get('author', intance.author)
#         intance.title = validated_data.get('title', intance.title)
#         intance.description = validated_data.get(
#             'description', intance.description
#         )
#         intance.body = validated_data.get('body', intance.body)
#         intance.location = validated_data.get('location', intance.location)
#         intance.publication_date = validated_data.get(
#             'publication_date', intance.publication_date
#         )
#         intance.active = validated_data.get('active', intance.active)
#         intance.save()
#         return intance
    
#     def validate(self, data):
#         '''Check if title and description are the same'''
#         if data['title'] == data['description']:
#             raise serializers.ValidationError(
#                 'Title and Description must be differents!'
#             )
#         return data

#     def validate_title(self, value):
#         if len(value) < 60:
#             raise serializers.ValidationError(
#                 'The Title has to be at least 60 chars long!'
#             )
#         return value