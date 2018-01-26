from rest_framework import serializers

from .models import Person


class BirthdaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'birthday')
