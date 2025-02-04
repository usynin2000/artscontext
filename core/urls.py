from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import (
    home_view,
    painting_view,
    paintings_view,
    post_page_view,
    contacts_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("post/<slug>/", post_page_view, name="post-page"),
    path("paintings/", paintings_view, name="paintings"),
    path("painting/<slug>", painting_view, name="painting-detail"),
    path("contacts/", contacts_view, name="contacts"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
