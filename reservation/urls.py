from django.urls import path

from reservation.apps import ReservationConfig
from reservation.views import HomeViews, AboutRestaurantViews, ReservationCreate, TableCreate, TableList, TableDetail, TableUpdate, TableDelete

app_name = ReservationConfig.name

urlpatterns = [
    path("", HomeViews.as_view(), name="home"),
    path("restaurant/", AboutRestaurantViews.as_view(), name="restaurant"),
    path("reservation/", ReservationCreate.as_view(), name="reservation_create"),
    path("tables/", TableList.as_view(), name="table_list"),
    path("table/<int:pk>/", TableDetail.as_view(), name="table_detail"),
    path("table/create/", TableCreate.as_view(), name="table_create"),
    path("table/<int:pk>/delete/", TableDelete.as_view(), name="table_delete"),
    path("table/<int:pk>/update/", TableUpdate.as_view(), name="table_update"),
]
