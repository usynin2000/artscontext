from django.shortcuts import get_object_or_404, redirect, render

from .models import News, Review

# Create your views here.


def home_view(request):
    news_list = News.objects.all()

    return render(request, "index.html", context={"news_list": news_list})


def post_page_view(request, slug):
    post = get_object_or_404(News, slug=slug)

    return render(request, "post_page.html", {"post": post})


def paintings_view(request):
    paintings = Review.objects.all()

    return render(request, "paintings.html", {"paintings": paintings})


def painting_view(request, slug):
    painting = get_object_or_404(Review, slug=slug)
    return render(request, "painting_page.html", {"painting": painting})


def contacts_view(request):
    return render(request, "contacts.html")
