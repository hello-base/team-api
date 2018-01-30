from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    nickname = serializers.CharField(source='caster.nickname')
    kamioshi = serializers.CharField(source='caster.kamioshi')
    oshi_overall = serializers.CharField(source='caster.oshi_overall')
    oshi_current = serializers.CharField(source='caster.oshi_current')

    class Meta:
        model = User
        fields = ('username', 'nickname', 'biography', 'kamioshi',
            'oshi_overall', 'oshi_current')
