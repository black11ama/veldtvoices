# Generated by Django 5.1.5 on 2025-01-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
