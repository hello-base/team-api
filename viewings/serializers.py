from rest_framework import serializers

from .models import Viewing


class ViewingSerializer(serializers.HyperlinkedModelSerializer):
    episode = serializers.StringRelatedField()

    class Meta:
        model = Viewing
        fields = ('pk', 'episode', 'headline', 'performer', 'song',
            'url', 'embed_url')
