from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True, primary_key=True)

    def __str__(self):
        return self.name


class Item(models.Model):

    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    parent_item = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default='first_menu')

    def __str__(self):
        return self.name
