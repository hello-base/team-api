from rest_framework import serializers

from .models import Episode


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'
