from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Модель пользователь"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = PhoneNumberField(
        verbose_name="Телефон", null=True, blank=True, help_text="Введите номер телефона", region="RU"
    )
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", null=True, blank=True, help_text="Загрузите свой аватар"
    )
    tg_name = models.CharField(
        max_length=50, verbose_name="Телеграм-ник", null=True, blank=True, help_text="Введите телеграм-ник"
    )
    token = models.CharField(max_length=100, verbose_name="Token", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
