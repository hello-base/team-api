from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    episode = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = ('pk', 'episode', 'headline', 'category', 'description',
            'images', 'references', 'sources')
