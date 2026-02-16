from datetime import date

from reservation.models import Table, Reservation

import factory
from factory.django import DjangoModelFactory
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

from users.models import User


def create_dummy_image():
    """Создаёт простое изображение в памяти для тестов"""
    image = Image.new('RGB', (100, 100), color='blue')  # Синий квадрат 100x100
    buffer = BytesIO()
    image.save(buffer, format='JPEG')
    buffer.seek(0)
    return ContentFile(buffer.read(), name='test_table.jpg')


class TableFactory(DjangoModelFactory):
    class Meta:
        model = Table

    table_number = factory.Sequence(lambda n: n + 1)  # 1, 2, 3, 4...
    location = factory.Faker('sentence', nb_words=4, locale='ru_RU')  # "Стол у окна с видом"
    photo_table = factory.LazyFunction(create_dummy_image)  # Генерируем изображение при создании
    table_capacity = factory.Faker('random_int', min=1, max=10)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email", locale="en_US")  # Уникальный email
    phone = factory.Faker("phone_number", locale="ru_RU")  # Российский формат
    avatar = None
    tg_name = factory.LazyAttribute(lambda obj: f"@{obj.email.split('@')[0]}")
    token = factory.Faker("uuid4")  # Уникальный токен
    password = factory.PostGenerationMethodCall('set_password', 'secret123')


class ReservationFactory(DjangoModelFactory):
    class Meta:
        model = Reservation

    date_reservation = factory.LazyFunction(lambda: date(2025, 9, 17))
    time_reservation = factory.Faker("time")
    count_people = factory.Faker("random_int", min=2, max=10)
    customer = factory.SubFactory(UserFactory)
    table = factory.SubFactory(TableFactory)
    wishes = factory.Faker('sentence', nb_words=10, locale='ru_RU')
    count_hours = factory.Faker('random_int', min=2, max=6)
