# api/serializers.py

from rest_framework import serializers
from .models import Carrier, Flight, FlightBooking
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
import json

class CarrierSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Carrier
        fields = ('id', 'carrier_name')


class FlightSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    carrier = CarrierSerializer()


    def create(self, data):
    	carrier_name =  data["carrier"]["carrier_name"]
        carrier, __ = Carrier.objects.get_or_create(carrier_name=carrier_name)
        

        return Flight.objects.create(flight_name=data["flight_name"], \
        				destination=data["destination"], \
        				eta=data["eta"], \
        				etd=data["etd"], \
        				price=data["price"], \
        				carrier=carrier)


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Flight
        fields = ('id', 'flight_name', 'carrier', 'destination', 'eta', 'etd', 'price')


class FlightBookingSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    flight = FlightSerializer()

    def create(self, data):
        flight_name =  data["flight"]["flight_name"]
        print flight_name
        try:
        	flight, response = Flight.objects.get_or_create(flight_name=flight_name)
        except:
        	flight, response = Flight.objects.filter(flight_name=flight_name)
        print flight
        print response
        booking = FlightBooking.objects.create(flight=flight)
        #print booking
        return booking


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = FlightBooking
        fields = ('id', 'flight')