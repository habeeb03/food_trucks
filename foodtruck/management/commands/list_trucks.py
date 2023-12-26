from django.core.management.base import BaseCommand
from foodtruck.utils import find_nearby_food_trucks


class Command(BaseCommand):
    help = 'Find nearby food trucks'

    def add_arguments(self, parser):
        parser.add_argument('latitude', type=float, help='Latitude for the search')
        parser.add_argument('longitude', type=float, help='Longitude for the search')
        parser.add_argument('--page-size', type=int, default=10, help='Number of items per page')

    def handle(self, *args, **kwargs):
        latitude = kwargs['latitude']
        longitude = kwargs['longitude']
        page_size = kwargs['page_size']

        start_index = 0

        while True:
            nearby_food_trucks = find_nearby_food_trucks(latitude, longitude)[start_index:start_index + page_size]

            if not nearby_food_trucks:
                if start_index == 0:
                    self.stdout.write(self.style.ERROR('No trucks found!'))
                break

            for truck in nearby_food_trucks:
                self.stdout.write(self.style.SUCCESS(f'Food Truck: {truck.applicant} - Distance: {truck.distance} km'))

            start_index += page_size
