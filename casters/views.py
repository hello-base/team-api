from django.shortcuts import render

from rest_framework import viewsets

from .models import Caster
from .serializers import CasterSerializer


class CasterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Caster.objects.all()
    serializer_class = CasterSerializer
