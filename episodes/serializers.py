from rest_framework import serializers

from .models import Corner, Episode


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('number', 'date')


class CornerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Corner
        fields = ('name', 'slug', 'category', 'description')
