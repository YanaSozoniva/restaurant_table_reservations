from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config import settings

urlpatterns = [
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
    path("", include("reservation.urls", namespace="reservation")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
