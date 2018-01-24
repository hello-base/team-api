import uuid

from django.db import models

from model_utils import Choices


class Viewing(models.Model):
    CATEGORY = Choices(
        ('performance', 'Performance'),
        ('release', 'Release'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    episode = models.ForeignKey('episodes.Episode', on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    performer = models.CharField(max_length=60)
    song = models.CharField(max_length=255)

    url = models.URLField()
    embed_url = models.URLField()

    def __str__(self):
        return self.headline
