from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings

urlpatterns = [
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
    path("", include("reservation.urls", namespace="reservation")),
    path("admin_page/", include("admin_page.urls", namespace="admin_page")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
