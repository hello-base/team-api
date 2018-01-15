import uuid

from datetime import date

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    episode = models.ForeignKey('episodes.Episode', on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)

    # Raw fields (newline-delimited)
    raw_images = models.TextField('images', blank=True)
    raw_references = models.TextField('references', blank=True)
    raw_sources = models.TextField('sources', blank=True)

    class Meta:
        ordering = ['episode', 'category', 'date']

    def __str__(self):
        return self.headline

    @property
    def images(self):
        return self.raw_images.splitlines()

    @property
    def references(self):
        return self.raw_references.splitlines()

    @property
    def sources(self):
        return self.raw_sources.splitlines()
