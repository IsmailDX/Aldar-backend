# Generated by Django 5.0 on 2023-12-08 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_properties_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Properties',
            new_name='PropertiesDetails',
        ),
    ]
