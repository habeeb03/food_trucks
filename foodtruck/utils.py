from django.db.models import F, ExpressionWrapper, fields
from django.db.models.functions import ACos, Cos, Sin, Radians
from .models import Truck


def find_nearby_food_trucks(latitude, longitude, max_distance=5):
    """
    Find nearby food trucks based on geographical coordinates.

    Parameters:
    - latitude (float): The latitude of the location.
    - longitude (float): The longitude of the location.
    - max_distance (float, optional): Maximum distance (in kilometers) to consider for proximity. Default is 5 km.

    Returns:
    - list: A list of food trucks within the specified maximum distance from the given coordinates.

    Example:
    >>> nearby_trucks = find_nearby_food_trucks(37.7749, -122.4194, max_distance=3)
    >>> print(nearby_trucks)
    [ <FoodTruck1>, <FoodTruck2>, ... ]

    Note:
    The distance is calculated using the Haversine formula, which provides an approximation for short distances.
    """
    # Convert max_distance from kilometers to degrees (approximate)
    max_distance_degrees = max_distance / 111.32

    # Calculate the latitude and longitude range
    min_latitude = latitude - max_distance_degrees
    max_latitude = latitude + max_distance_degrees
    min_longitude = longitude - max_distance_degrees
    max_longitude = longitude + max_distance_degrees

    nearby_trucks = Truck.objects.filter(
        latitude__range=(min_latitude, max_latitude),
        longitude__range=(min_longitude, max_longitude)
    ).annotate(
        distance=ExpressionWrapper(
            6371 * ACos(
                Cos(Radians(latitude)) * Cos(Radians(F('latitude'))) *
                Cos(Radians(F('longitude')) - Radians(longitude)) +
                Sin(Radians(latitude)) * Sin(Radians(F('latitude')))
            ),
            output_field=fields.FloatField()
        )
    ).filter(distance__lte=max_distance).order_by('distance')

    return nearby_trucks
