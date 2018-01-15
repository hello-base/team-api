from django.shortcuts import render

from rest_framework import viewsets

from .models import Corner, Episode
from .serializers import CornerSerializer, EpisodeSerializer


class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    lookup_field = 'number'


class CornerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Corner.objects.all()
    serializer_class = CornerSerializer
