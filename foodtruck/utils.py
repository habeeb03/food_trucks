from django.db.models import F, ExpressionWrapper, fields
from django.db.models.functions import ACos, Cos, Sin, Radians
from .models import Truck


def find_nearby_food_trucks(latitude, longitude, max_distance=5):
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
