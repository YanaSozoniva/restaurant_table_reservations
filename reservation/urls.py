from django.urls import path

from reservation.apps import ReservationConfig
from reservation.views import (AboutRestaurantViews, HomeViews, ReservationCreate, ReservationDetail, ReservationList,
                               ReservationDelete, TableCreate, TableDelete, TableDetail, TableList, TableUpdate)

app_name = ReservationConfig.name

urlpatterns = [
    path("", HomeViews.as_view(), name="home"),
    path("restaurant/", AboutRestaurantViews.as_view(), name="restaurant"),
    path("reservation/create/", ReservationCreate.as_view(), name="reservation_create"),
    path("reservation/<int:pk>/", ReservationDetail.as_view(), name="reservation_detail"),
    path("table/<int:pk>/delete/", ReservationDelete.as_view(), name="reservation_delete"),
    path("reservation/", ReservationList.as_view(), name="reservation_list"),
    path("tables/", TableList.as_view(), name="table_list"),
    path("table/<int:pk>/", TableDetail.as_view(), name="table_detail"),
    path("table/create/", TableCreate.as_view(), name="table_create"),
    path("table/<int:pk>/delete/", TableDelete.as_view(), name="table_delete"),
    path("table/<int:pk>/update/", TableUpdate.as_view(), name="table_update"),
]
