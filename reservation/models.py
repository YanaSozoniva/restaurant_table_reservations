from django.core.validators import MinValueValidator
from django.db import models

from users.models import User
from reservation.validator import FileSizeValidator, ImageFormatValidator


class Table(models.Model):
    """Модель Стол для бронирования"""

    table_number = models.PositiveIntegerField(verbose_name="Номер стола", help_text="Укажите номер стола")
    location = models.CharField(
        max_length=200, verbose_name="Расположение", help_text="Укажите расположение стола", null=True, blank=True
    )
    photo_table = models.ImageField(
        upload_to="photos/",
        verbose_name="Изображение",
        help_text="Загрузите фото стола",
        blank=True,
        null=True,
        validators=[FileSizeValidator(), ImageFormatValidator()],
    )
    table_capacity = models.PositiveIntegerField(
        verbose_name="Вместительность стола",
        default=1,
        help_text="Укажите сколько максимум человек может поместиться за столом",
    )

    def __str__(self):
        return f"{self.table_number} - вместительность {self.table_capacity} человек"

    class Meta:
        verbose_name = "Стол"
        verbose_name_plural = "Столы"


class Reservation(models.Model):
    """Модель Бронирование столиков"""

    date_reservation = models.DateField(
        verbose_name="Дата бронирования столика", help_text="Выберите число, на которое хотите забронировать столик"
    )
    time_reservation = models.TimeField(
        verbose_name="Время бронирования столика", help_text="Выберите время, на которое хотите забронировать столик"
    )
    count_people = models.PositiveIntegerField(
        default=2,
        verbose_name="Количество человек",
        help_text="Введите количество человек, но не меньше 2x",
        validators=[MinValueValidator(2)],
    )
    customer = models.ForeignKey(
        User,
        verbose_name="Заказчик брони",
        help_text="Укажите номер стола, который хотите забронировать",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="reservation",
    )

    table = models.ForeignKey(Table, verbose_name="Номер стола", on_delete=models.CASCADE, related_name="reservation")

    wishes = models.TextField(
        verbose_name="Особые пожелания", blank=True, null=True, help_text="Напишите Ваши пожелания"
    )

    count_hours = models.PositiveIntegerField(
        default=2,
        verbose_name="Количество часов брони",
        help_text="Введите количество часов, на сколько хотите забронировать столик, но не меньше 2x",
        validators=[MinValueValidator(2)],
    )

    def __str__(self):
        return (
            f"Заказчик {self.customer} забронировал столик {self.table}"
            f" на {self.date_reservation} {self.time_reservation}"
        )

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"


class Restaurant(models.Model):
    """ Модель ресторан """
    name = models.CharField(max_length=200, verbose_name="Название ресторана")
    logo = models.ImageField(upload_to="photos/", verbose_name="Логотип ресторана",
                             validators=[FileSizeValidator(), ImageFormatValidator()],)
    story = models.TextField(verbose_name="История ресторана")
    mission = models.TextField(verbose_name="Миссия")

    class Meta:
        verbose_name = "ресторан"
        verbose_name_plural = "рестораны"


class Employee(models.Model):
    """ Модель сотрудники ресторана """
    name = models.CharField(max_length=200, verbose_name="Фамилия и имя сотрудника")
    photo_employee = models.ImageField(upload_to="photos/", verbose_name="Фото сотрудника",
                             validators=[FileSizeValidator(), ImageFormatValidator()])
    job_title = models.CharField(max_length=200, verbose_name="Должность")
    description = models.TextField(verbose_name="Комментарии о сотруднике", null=True, blank=True)
