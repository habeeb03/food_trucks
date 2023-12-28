from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import FoodTruckSerializer
from django.views.generic import View
from .utils import find_nearby_food_trucks


class IndexView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'foodtruck/index.html')


class FoodTruckList(ListAPIView):
    serializer_class = FoodTruckSerializer
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        latitude = float(request.GET.get('lat', 0))
        longitude = float(request.GET.get('lng', 0))

        return find_nearby_food_trucks(latitude, longitude)
