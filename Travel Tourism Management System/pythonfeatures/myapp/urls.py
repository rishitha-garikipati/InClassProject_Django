from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("weatherinfo/", views.weatherinfo, name="weatherinfo"),
    path("contactmail/",views.contactmail,name="contactmail"),
]
