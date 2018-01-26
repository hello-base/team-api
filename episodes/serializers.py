from rest_framework import serializers

from people.serializers import BirthdaySerializer

from .models import Corner, Episode


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    birthdays = BirthdaySerializer(many=True)

    class Meta:
        model = Episode
        fields = ('number', 'date', 'birthdays')


class CornerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Corner
        fields = ('name', 'slug', 'category', 'description')
