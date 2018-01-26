
from django.shortcuts import render

from django_filters import rest_framework as filters
from rest_framework import viewsets

from .models import Viewing
from .serializers import ViewingSerializer


class ViewingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Viewing.objects.all()
    serializer_class = ViewingSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('episode__number',)
