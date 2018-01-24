from django.contrib import admin

from .models import Viewing


class ViewingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Viewing, ViewingAdmin)
