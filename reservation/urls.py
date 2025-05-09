from django.urls import path
from django.views.decorators.cache import cache_page

from reservation.apps import ReservationConfig
from reservation.views import (AboutRestaurantViews, HomeViews, ReservationCreate, ReservationDetail, ReservationList,
                               ReservationDelete, TableCreate, TableDelete, TableDetail, TableList, TableUpdate,
                               get_available_tables, ReservationUpdate)

app_name = ReservationConfig.name

urlpatterns = [
    path("", cache_page(60*10)(HomeViews.as_view()), name="home"),
    path("restaurant/",  cache_page(60*10)(AboutRestaurantViews.as_view()), name="restaurant"),
    path("reservation/create/", ReservationCreate.as_view(), name="reservation_create"),
    path("reservation/<int:pk>/", ReservationDetail.as_view(), name="reservation_detail"),
    path("reservation/<int:pk>/update/", ReservationUpdate.as_view(), name="reservation_update"),
    path("reservation/<int:pk>/delete/", ReservationDelete.as_view(), name="reservation_delete"),
    path("reservation/", ReservationList.as_view(), name="reservation_list"),
    path("tables/", TableList.as_view(), name="table_list"),
    path("table/<int:pk>/", TableDetail.as_view(), name="table_detail"),
    path("table/create/", TableCreate.as_view(), name="table_create"),
    path("table/<int:pk>/delete/", TableDelete.as_view(), name="table_delete"),
    path("table/<int:pk>/update/", TableUpdate.as_view(), name="table_update"),
    path('get-available-tables/', get_available_tables, name='get_available_tables'),
]
