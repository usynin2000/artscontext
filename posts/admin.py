from django.contrib import admin
from .models import News, Review, Artist, Tag

# Register your models here.
admin.site.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(Review)
admin.site.register(Artist)
admin.site.register(Tag)
