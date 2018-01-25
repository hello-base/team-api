import uuid

from django.db import models

from birthday.fields import BirthdayField
from birthday.managers import BirthdayManager


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    birthday = BirthdayField()
    objects = BirthdayManager()

    def __str__(self):
        return self.name
