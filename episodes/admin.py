from django.contrib import admin

from .models import Corner, Episode


class EpisodeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Episode, EpisodeAdmin)


class CornerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Corner, CornerAdmin)
