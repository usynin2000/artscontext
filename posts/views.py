from django.shortcuts import render, redirect, get_object_or_404
from .models import News


# Create your views here.


def home_view(request):
    news_list = News.objects.all()

    return render(request, "index.html", context={"news_list": news_list})


def post_page_view(request, slug):
    post = get_object_or_404(News, slug=slug)
    context = {"post": post}
    return render(request, "post_page.html", context)


def carousel_view(request):
    images = [
        {'url': 'https://live.staticflickr.com/65535/50618365686_36f887ab88_c.jpg', 'alt': 'Beautiful Mountain'},
        {'url': 'https://live.staticflickr.com/65535/49909538937_3255dcf9e7_b.jpg', 'alt': 'Serene Lake'},
        {'url': 'https://live.staticflickr.com/65535/53642930419_8d48cf95b6_z.jpg', 'alt': 'Forest Path'},
    ]
    caption = 'Enjoy our photo gallery showcasing stunning landscapes and serene environments.'
    return render(request, 'carousel.html', {'images': images, 'caption': caption})