# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Carrier, Flight, FlightBooking

admin.site.register(Carrier)
admin.site.register(Flight)
admin.site.register(FlightBooking)
# Register your models here.
