from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CarrierView, CarrierDetailsView, FlightView, FlightDetailsView, FlightBookingView, FlightBookingDetailsView


urlpatterns = {
    url(r'^carriers/$', CarrierView.as_view(), name="carrier_view"),
    url(r'^carriers/(?P<pk>[0-9]+)/$',
        CarrierDetailsView.as_view(), name="carrier_details"),
    url(r'^flights/$', FlightView.as_view(), name="flight_view"),
    url(r'^flights/(?P<pk>[0-9]+)/$',
        FlightDetailsView.as_view(), name="flight_details"),
    url(r'^bookings/$', FlightBookingView.as_view(), name="booking_view"),
    url(r'^bookings/(?P<pk>[0-9]+)/$',
        FlightBookingDetailsView.as_view(), name="booking_details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)