from django.contrib import admin

from .models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
