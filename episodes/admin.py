from django.contrib import admin

from .models import Episode


class EpisodeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Episode, EpisodeAdmin)
