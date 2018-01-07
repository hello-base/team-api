import uuid

from datetime import date

from django.db import models


class Episode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.PositiveSmallIntegerField()
    date = models.DateField(default=date.today)
