from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import News


@receiver(pre_save, sender=News)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        # Генерируем slug из title
        instance.slug = slugify(instance.title)
        # Проверяем уникальность slug и, если нужно, добавляем число
        original_slug = instance.slug
        counter = 1
        while News.objects.filter(slug=instance.slug).exists():
            instance.slug = f"{original_slug}-{counter}"
            counter += 1
