import uuid

from datetime import date

from django.db import models

from model_utils import Choices

from people.models import Person


class Episode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.PositiveSmallIntegerField()
    date = models.DateField(default=date.today)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%d' % self.number

    @property
    def birthdays(self):
        return Person.objects.get_upcoming_birthdays(after=self.date)

class Corner(models.Model):
    CATEGORY = Choices(
        ('activity', 'Activity'),
        ('game', 'Game'),
        ('talk', 'Talk'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.CharField(max_length=8, choices=CATEGORY, default=CATEGORY.activity)
    description = models.TextField()

    def __str__(self):
        return self.name
