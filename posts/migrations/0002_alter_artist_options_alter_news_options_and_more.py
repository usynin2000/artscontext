# Generated by Django 5.0.1 on 2024-08-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="artist",
            options={"verbose_name": "Художник", "verbose_name_plural": "Художники"},
        ),
        migrations.AlterModelOptions(
            name="news",
            options={"verbose_name": "Новость", "verbose_name_plural": "Новости"},
        ),
        migrations.AlterModelOptions(
            name="review",
            options={
                "verbose_name": "Обзор картин",
                "verbose_name_plural": "Обзоры картин",
            },
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "Тэг", "verbose_name_plural": "Тэги"},
        ),
        migrations.AddField(
            model_name="news",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="review",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
