from django.contrib import admin
from .models import Flight,Passenger,Reservation
# Register your models here.

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['flight_number','operating_airline','departure_city','arrival_city','date_of_departure','estimated_time_of_departure']

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','middle_name','email','phone']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['flight','passenger']

