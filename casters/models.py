from django.db import models
from django.contrib.auth.models import User


class Caster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, blank=True)
    kamioshi = models.CharField(max_length=255, blank=True)
    oshi_overall = models.CharField(max_length=255, blank=True)
    oshi_current = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
