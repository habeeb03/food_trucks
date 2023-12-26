from django.db import models


class Truck(models.Model):
    applicant = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.applicant
