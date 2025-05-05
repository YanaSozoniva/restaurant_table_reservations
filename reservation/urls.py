from django.urls import path

from reservation.apps import ReservationConfig
from reservation.views import HomeViews, AboutRestaurantViews, ReservationCreate

app_name = ReservationConfig.name

urlpatterns = [
    path("", HomeViews.as_view(), name="home"),
    path("restaurant/", AboutRestaurantViews.as_view(), name="restaurant"),
    path("reservation/", ReservationCreate.as_view(), name="reservation_create"),
]
