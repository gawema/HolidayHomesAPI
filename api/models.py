from django.db import models
from django.contrib.auth.models import User

class House(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    floor = models.CharField(max_length=10)
    direction = models.CharField(max_length=3)
    vacancy = models.CharField(max_length=50)
    price_per_night = models.CharField(max_length=20)
    longitude = models.CharField(max_length=50)
    laditude = models.CharField(max_length=50)
    owner = models.ForeignKey(User, related_name='house', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, related_name='booking', on_delete=models.CASCADE)
    house = models.ForeignKey(House, related_name='booking', on_delete=models.CASCADE)
    date_of_reservation = models.DateField()
    date_booking_from = models.DateField()
    date_booking_to = models.DateField()
    status: models.CharField(max_length=50)

class Facility(models.Model):
    name = models.CharField(max_length=200)
       
    def __str__(self):
        return self.name

class HouseFacility(models.Model):
    house = models.ForeignKey(House, related_name='house', on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, related_name='facility', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.house)+' with: '+str(self.facility)

class Gallery(models.Model):
    image = models.TextField()
    house = models.ForeignKey(House, related_name='gallery', on_delete=models.CASCADE)

