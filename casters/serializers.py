from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    nickname = serializers.CharField(source='caster.nickname')
    biography = serializers.CharField(source='caster.biography')
    kamioshi = serializers.CharField(source='caster.kamioshi')
    order = serializers.IntegerField(source='caster.order')
    oshi_overall = serializers.CharField(source='caster.oshi_overall')
    oshi_current = serializers.CharField(source='caster.oshi_current')
    oshi_current = serializers.CharField(source='caster.oshi_current')

    class Meta:
        model = User
        fields = ('username', 'nickname', 'biography', 'kamioshi',
            'order', 'oshi_overall', 'oshi_current')
