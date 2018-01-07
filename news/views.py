
from django.shortcuts import render

from django_filters import rest_framework as filters
from rest_framework import viewsets

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('episode__number',)
