# Generated by Django 5.1.5 on 2025-01-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='cover',
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
