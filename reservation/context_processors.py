from reservation.models import Restaurant


def restaurant_data(request):
    """Передача данные из модели ресторан для дальнейшего использования в любом шаблоне"""

    restaurant = Restaurant.objects.first()
    if restaurant:
        return {
            "restaurant_name": restaurant.name,
            "restaurant_logo": restaurant.logo,
            "restaurant_mission": restaurant.mission,
        }

    return {
        "restaurant_name": "Название ресторана",
        "restaurant_logo": None,
        "restaurant_mission": "Миссия ресторана",
    }
