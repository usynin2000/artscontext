from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    ### добавить images и еще что-то


class Review(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    # добавить images(желательно несколкьо) тип картины Барокко и тд, год создания можно, и еще какие-либо данные


class Artist(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    ###  возможно еще стиль или эпоху


class Tags(models.Model):
    name = models.CharField(max_length=120)
    ### связь с новостями или типами продумать
