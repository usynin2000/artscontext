"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import (carousel_view, home_view, painting_view,
                         paintings_view, post_page_view, contacts_view)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("post/<slug>/", post_page_view, name="post-page"),
    path("carousel/", carousel_view, name="carousel"),
    path("paintings/", paintings_view, name="paintings"),
    path("painting/<slug>", painting_view, name="painting-detail"),
    path("contacts/", contacts_view, name="contacts")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
