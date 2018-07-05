"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from flight_mgt import views
from rest_framework.authtoken import views as vw

router = routers.DefaultRouter()
#router.register(r'carrier', views.CarrierViewSet)
#router.register(r'flight', views.FlightViewSet)
#router.register(r'flight_book', views.FlightBookingViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('flight_mgt.urls')), # Add this line
    url(r'^', include('rest_framework.urls')),
    url(r'^api-token-auth/', vw.obtain_auth_token),

]
