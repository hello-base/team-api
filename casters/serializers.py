from rest_framework import serializers

from .models import Caster


class CasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Caster
        fields = ('user', 'nickname', 'kamioshi', 'oshi_overall',
            'oshi_current')
