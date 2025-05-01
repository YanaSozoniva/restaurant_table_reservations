from django.urls import path

from reservation.apps import ReservationConfig
from reservation.views import HomeViews

app_name = ReservationConfig.name

urlpatterns = [
    path("", HomeViews.as_view(), name="home"),
]
