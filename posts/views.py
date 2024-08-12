from django.shortcuts import render, redirect, get_object_or_404
from .models import News


# Create your views here.


def home_view(request):
    news_list = News.objects.all()

    return render(request, "index.html", context={"news_list": news_list})


def post_page_view(request):
    return render(request, "post_page.html")