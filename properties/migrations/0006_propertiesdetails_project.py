# Generated by Django 5.0 on 2023-12-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_alter_propertiesdetails_locationdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertiesdetails',
            name='project',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
