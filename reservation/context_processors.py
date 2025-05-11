from reservation.models import Restaurant


def restaurant_data(request):
    """ Передача данные из модели ресторан для дальнейшего использования в любом шаблоне """
    try:
        restaurant = Restaurant.objects.first()
        return {
            'restaurant_name': restaurant.name,
            'restaurant_logo': restaurant.logo,
            'restaurant_mission': restaurant.mission
        }
    except:
        return {
            'restaurant_name': 'Название ресторана',
            'restaurant_logo': None,
            'restaurant_mission': 'Миссия ресторана'
        }
