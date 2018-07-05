# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Carrier(models.Model):
    # song title
    carrier_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}".format(self.carrier_name)


class Flight(models.Model):
    # song title
    flight_name = models.CharField(max_length=255, null=False)
    carrier = models.ForeignKey(Carrier, related_name='carrier', default='')
    #carrier = models.CharField(max_length=255, null=False)
    destination = models.CharField(max_length=255, null=False)
    eta = models.DateTimeField()
    etd = models.DateTimeField()
    price = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}".format(self.flight_name)


class FlightBooking(models.Model):
    # song title
    flight = models.ForeignKey(Flight, related_name='flight', default='')

    def __str__(self):
        return "{}".format(self.flight)
