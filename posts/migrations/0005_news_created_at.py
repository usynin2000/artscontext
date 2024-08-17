# Generated by Django 5.0.1 on 2024-08-17 00:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_rename_image_news_image_1_news_image_2_news_image_3_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
