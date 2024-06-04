from django.shortcuts import render
from .models import Flight,Passenger,Reservation
from .serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.
#Custome Function
@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departure_city=request.data['departure_city'],arrival_city=request.data['arrival_city'],date_of_departure=request.data['date_of_departure'])
    serializer = FlightSerializer(flights,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    print('request.data--',request.data)
    flight = Flight.objects.get(id=request.data['flightID'])

    passenger = Passenger()
    passenger.first_name = request.data['first_name']
    passenger.last_name = request.data['last_name']
    passenger.middle_name = request.data['middle_name']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']

    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer        
