from datetime import time

from reservation.models import Reservation, Table
from users.models import User


def add_hours(t, hours):
    """Функция вычисления времени освобождения столика"""
    total_seconds = (t.hour + hours) * 3600 + t.minute * 60 + t.second
    new_hour = (total_seconds // 3600) % 24
    remaining_seconds = total_seconds % 3600
    new_minute = remaining_seconds // 60
    new_second = remaining_seconds % 60

    return time(new_hour, new_minute, new_second)


def get_free_tables(date_reservation, time_reservation):
    """Выборка свободных столиков"""
    reservations = Reservation.objects.filter(date_reservation=date_reservation)

    if not reservations:
        return Table.objects.all()

    reserved_tables = []
    for reservation in reservations:
        new_time = add_hours(reservation.time_reservation, reservation.count_hours + 1)
        if time_reservation >= reservation.time_reservation and time_reservation < new_time:
            reserved_tables.append(reservation.table.id)

    available_tables = Table.objects.exclude(id__in=reserved_tables)

    return available_tables


def get_statistical_data():
    """Функция получения статистической информации по количеству столиков, бронирования и т.п."""
    context = {
        "reservations_count": Reservation.objects.count(),
        "tables_count": Table.objects.count(),
        "users_count": User.objects.exclude(user_permissions__codename="can_change_content").count,
        "recent_reservations": Reservation.objects.select_related("customer", "table").order_by(
            "-date_reservation", "-time_reservation"
        )[:10],
    }
    return context
