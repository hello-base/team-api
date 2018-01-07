from django.shortcuts import render

from rest_framework import viewsets

from .models import Episode
from .serializers import EpisodeSerializer


class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
