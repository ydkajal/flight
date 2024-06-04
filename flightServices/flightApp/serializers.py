from rest_framework import serializers
from .models import Flight,Passenger,Reservation
import re

#second checked
def isFlightNumberValid(data):
    print('data--')
    print(data['flight_number'])
    return data

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [isFlightNumberValid]  #when validation method is declared outside serializers class 

    #custom validation-Field specific-which is firstly checked before any validate method
    def validate_flight_number(self,flight_number):
        if (re.match("^[a-zA-Z0-9]*$",flight_number)==None):
            raise serializers.ValidationError('Invalid flight number. Make sure it is alpha numeric')
        return flight_number
    
    #last checked
    def validate(self, data):
        print('data')
        print(data['flight_number'])
        return data
    


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'        

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'                