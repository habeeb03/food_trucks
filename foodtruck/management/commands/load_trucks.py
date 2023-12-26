import csv

from django.core.management import BaseCommand
from foodtruck.models import Truck


class Command(BaseCommand):
    help = 'Load truck from CSV to truck model'

    def handle(self, *args, **options):
        Truck.objects.all().delete()

        with open('food_truck.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                _, applicant, _, _, description, address, _, _, _, _, _, _, _, _, latitude, longitude, _, _, _, _, _, _, _, _, _, _, _, _, _ = row
                Truck.objects.create(
                    applicant=applicant,
                    latitude=latitude,
                    longitude=longitude,
                    address=address,
                    description=description
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
