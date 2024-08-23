from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(blank=True, max_length=130)
    image_1 = models.ImageField(upload_to="images/", null=True, blank=True)
    image_2 = models.ImageField(upload_to="images/", null=True, blank=True)
    image_3 = models.ImageField(upload_to="images/", null=True, blank=True)
    image_4 = models.ImageField(upload_to="images/", null=True, blank=True)
    image_5 = models.ImageField(upload_to="images/", null=True, blank=True)
    image_6 = models.ImageField(upload_to="images/", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=True)

    @property
    def image_fields(self):
        return [
            getattr(self, f"image_{i}")
            for i in range(1, 7)
            if getattr(self, f"image_{i}")
        ]

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Новости"
        verbose_name = "Новость"


class Review(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(blank=True, max_length=130)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="paintings/", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=True)

    # добавить images(желательно несколкьо) тип картины Барокко и тд, год создания можно, и еще какие-либо данные

    def __str__(self):
        name = str(self.title) + " (" + str(self.artist) + ")"
        return name

    def save(self, *args, **kwargs):
        if not self.slug:
            # Генерируем slug из title
            self.slug = slugify(self.title)
            # Проверяем уникальность slug и, если нужно, добавляем число
            original_slug = self.slug
            counter = 1
            while Review.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Обзоры картин"
        verbose_name = "Обзор картин"

        ordering = ["-created_at"]


class Artist(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    ###  возможно еще стиль или эпоху

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Художники"
        verbose_name = "Художник"


class Tag(models.Model):
    name = models.CharField(max_length=120)
    ### связь с новостями или типами продумать

    class Meta:
        verbose_name_plural = "Тэги"
        verbose_name = "Тэг"
