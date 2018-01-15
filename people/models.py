import birthday
import uuid

from django.db import models


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    birthday = birthday.fields.BirthdayField()

    objects = birthday.managers.BirthdayManager()

    def __str__(self):
        return self.name
