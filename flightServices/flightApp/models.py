from django.db import models

#for creating tokens automatically
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    operating_airline = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=20)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()

class Passenger(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
       
class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def createAuthToken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)