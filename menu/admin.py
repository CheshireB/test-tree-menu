from django.contrib import admin

from .models import Tree, Node


class TreeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']


admin.site.register(Tree, TreeAdmin)
admin.site.register(Node, NodeAdmin)

