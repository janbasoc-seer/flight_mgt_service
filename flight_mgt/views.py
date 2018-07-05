# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#from django.contrib.auth.models import Carrier, Flight, FlightBooking
from rest_framework import viewsets
from rest_framework import generics
from .serializers import CarrierSerializer, FlightSerializer, FlightBookingSerializer
from .models import Carrier, Flight, FlightBooking



class CarrierView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class CarrierDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer



class FlightView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class FlightDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightBookingView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = FlightBooking.objects.all()
    serializer_class = FlightBookingSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class FlightBookingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = FlightBooking.objects.all()
    serializer_class = FlightBookingSerializer

