from django.urls import path

from admin_page.apps import AdminConfig
from admin_page.views import (AdminPageViews, EmployeeCreate, EmployeeDelete, EmployeeDetail, EmployeeList,
                              EmployeeUpdate, RestaurantDetail, RestaurantUpdate)

app_name = AdminConfig.name

urlpatterns = [
    path("admin_page/", AdminPageViews.as_view(), name="admin_page"),
    path("employee/", EmployeeList.as_view(), name="employee_list"),
    path("employee/<int:pk>/", EmployeeDetail.as_view(), name="employee_detail"),
    path("employee/create/", EmployeeCreate.as_view(), name="employee_create"),
    path("employee/<int:pk>/delete/", EmployeeDelete.as_view(), name="employee_delete"),
    path("employee/<int:pk>/update/", EmployeeUpdate.as_view(), name="employee_update"),
    path("restaurant/<int:pk>/update/", RestaurantUpdate.as_view(), name="restaurant_update"),
    path("restaurant/<int:pk>/", RestaurantDetail.as_view(), name="restaurant_detail"),
]
