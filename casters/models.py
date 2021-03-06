from django.db import models
from django.contrib.auth.models import User


class Caster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, blank=True)
    biography = models.TextField(blank=True)
    kamioshi = models.CharField(max_length=255, blank=True)
    oshi_overall = models.CharField('All-Time Favorites', max_length=255, blank=True)
    oshi_current = models.CharField('Current Favorites', max_length=255, blank=True)

    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.user.username
