# Generated by Django 2.0.4 on 2018-04-25 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='parent_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Node'),
        ),
        migrations.AlterField(
            model_name='node',
            name='tree',
            field=models.ForeignKey(default='first_tree', on_delete=django.db.models.deletion.CASCADE, to='menu.Tree'),
        ),
    ]