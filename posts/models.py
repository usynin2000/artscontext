from django.db import models


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    ### добавить images и еще что-то

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'





class Review(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    # добавить images(желательно несколкьо) тип картины Барокко и тд, год создания можно, и еще какие-либо данные

    class Meta:
        verbose_name_plural = 'Обзоры картин'
        verbose_name = 'Обзор картин'


class Artist(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    ###  возможно еще стиль или эпоху

    class Meta:
        verbose_name_plural = 'Художники'
        verbose_name = 'Художник'


class Tag(models.Model):
    name = models.CharField(max_length=120)
    ### связь с новостями или типами продумать

    class Meta:
        verbose_name_plural = 'Тэги'
        verbose_name = 'Тэг'
