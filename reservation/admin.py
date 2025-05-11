from django.contrib import admin

from reservation.models import Reservation, Table, Restaurant, Employee


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели бронирование"""

    list_display = (
        "id",
        "date_reservation",
        "time_reservation",
        "count_people",
        "customer",
        "table",
        "wishes",
        "count_hours",
    )
    list_filter = ("date_reservation", "time_reservation")
    search_fields = (
        "table",
        "customer",
        "date_reservation",
    )


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели столы"""

    list_display = ("id", "table_number", "location", "table_capacity")
    list_filter = ("table_number", "table_capacity")
    search_fields = ("table_number", "table_capacity")


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели ресторана"""

    list_display = ("id", "name", "logo", "story", "mission", "description")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели ресторана"""

    list_display = ("id", "name", "photo_employee", "job_title", "description")
    list_filter = ("name", "job_title")
    search_fields = ("name", "job_title")
