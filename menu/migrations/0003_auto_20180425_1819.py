# Generated by Django 2.0.4 on 2018-04-25 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20180425_1639'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Node',
            new_name='Item',
        ),
        migrations.RenameModel(
            old_name='Tree',
            new_name='Menu',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='parent_node',
            new_name='parent_item',
        ),
    ]
