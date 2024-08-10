from django.contrib import admin
from .models import News, Review, Artist, Tag

# Register your models here.
admin.site.register(News)
admin.site.register(Review)
admin.site.register(Artist)
admin.site.register(Tag)
