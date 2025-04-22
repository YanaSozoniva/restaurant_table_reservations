from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователь"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = PhoneNumberField(verbose_name="Телефон", null=True, blank=True, help_text="Введите номер телефона")
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", null=True, blank=True, help_text="Загрузите свой аватар"
    )
    country = models.CharField(max_length=35, verbose_name="Страна", blank=True, null=True, help_text="Укажите страну")
    token = models.CharField(max_length=100, verbose_name="Token", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

