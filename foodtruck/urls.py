from django.urls import path
from . import views

urlpatterns = [
    path("trucks/", views.FoodTruckList.as_view(), name='find-trucks')
]
