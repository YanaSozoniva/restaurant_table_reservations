from datetime import timedelta

from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail

from config import settings
from reservation.models import Reservation


@shared_task
def send_email_about_reservation():
    """Отправляет пользователю сообщение на почту о забронированном столики за час"""
    date_now = timezone.now().date()
    time_now = timezone.now() + timedelta(hours=1)
    time = time_now.time().replace(second=0, microsecond=0)

    reservations = Reservation.objects.filter(date_reservation=date_now, time_reservation=time)

    for reservation in reservations:
        subject = f"Бронирование столика {reservation.table.table_number} в ресторане"
        message = f"Вы забронировали столик на сегодня на {reservation.time_reservation} на {reservation.count_people} чел. Будем рады видеть Вас!"
        send_mail(subject, message, settings.EMAIL_HOST_USER, reservation.customer.email)
        # если есть телеграмм
        # if reservation.customer.tg_name:
        #     send_telegram_message(reservation.customer.tg_name, message)
