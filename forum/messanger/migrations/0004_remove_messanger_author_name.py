# Generated by Django 5.0.6 on 2024-05-25 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messanger', '0003_messanger_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messanger',
            name='author_name',
        ),
    ]