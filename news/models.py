import uuid

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    headline = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    description = models.TextField()

    images = models.TextField()
    sources = models.TextField()
