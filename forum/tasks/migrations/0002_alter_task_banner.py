# Generated by Django 5.0.6 on 2024-05-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='banner',
            field=models.ImageField(default='fallback.png', upload_to='media'),
        ),
    ]
