# Generated by Django 4.2.6 on 2023-11-01 08:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_news_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
