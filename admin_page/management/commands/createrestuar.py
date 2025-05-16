from django.core.management.base import BaseCommand

from reservation.models import Restaurant


class Command(BaseCommand):
    """Кастомная команда для создания информации о ресторане"""

    def handle(self, *args, **options):
        restaurant = Restaurant.objects.create(
            name="Сладкая жизнь",
            story="Ресторан 'Сладкая жизнь' открыл свои двери в 2025 году с целью создать место, где каждый "
            "сможет ощутить настоящую магию десертов. Начав с маленькой кондитерской, мы выросли "
            "в полноценный ресторан, сохранив при этом домашнюю атмосферу и любовь к традициям. За эти годы мы "
            "разработали более 200 уникальных рецептов и стали любимым местом для ценителей"
            " изысканных сладостей.",
            mission="Сладкая жизнь - это сладости на все случаи жизни, уютная атмосфера, дружный коллектив",
        )
        restaurant.save()
        self.stdout.write(self.style.SUCCESS(f"Successfully created restaurant {restaurant.name}"))
