# Generated by Django 4.2.6 on 2023-11-01 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='picture',
        ),
    ]
