from django.db import models

class Tree(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True, primary_key=True)

    def __str__(self):
        return self.name


class Node(models.Model):

    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    parent_node = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, default='first_tree')

    def __str__(self):
        return self.name
