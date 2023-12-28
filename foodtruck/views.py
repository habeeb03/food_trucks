from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import FoodTruckSerializer
from django.views.generic import View
from .utils import find_nearby_food_trucks


class IndexView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'foodtruck/index.html')


class FoodTruckList(ListAPIView):
    """
    API endpoint to retrieve a list of nearby food trucks based on geographical coordinates.

    Parameters:
    - lat (float): Latitude of the location.
    - lng (float): Longitude of the location.

    Returns:
    - JSON: A serialized list of nearby food trucks.

    Example:
    - Request:
      ```
      GET /api/food-trucks/?lat=37.7749&lng=-122.4194
      ```

    - Response:
      ```json
      [
        {
          "id": 1,
          "name": "Leo's Hot Dogs",
          "facility_type": "Push Cart",
          "food_items": "Hot dogs and related toppings: non-alcoholic beverages",
          "latitude": 37.760086931987,
          "longitude": -122.418806481101,
          "schedule": "09/20/2023 12:00:00 AM",
          "status": "APPROVED"
        },
        // Additional food truck objects...
      ]
      ```

    Note:
    The API uses the Haversine formula to calculate distances and returns a list of food trucks within a default distance of 5 kilometers.
    """
    serializer_class = FoodTruckSerializer
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        latitude = float(request.GET.get('lat', 0))
        longitude = float(request.GET.get('lng', 0))

        return find_nearby_food_trucks(latitude, longitude)
