from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets

from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def filter_queryset(self, queryset):
        queryset = super(UserViewSet, self).filter_queryset(queryset)
        return queryset.order_by('caster__order')
