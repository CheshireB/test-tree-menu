from django.contrib import admin

from .models import Menu, Item


class TreeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']


admin.site.register(Menu, TreeAdmin)
admin.site.register(Item, NodeAdmin)

