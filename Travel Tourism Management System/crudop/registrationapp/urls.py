from django.urls import path
from . import views

urlpatterns = [
    path('',views.homee,name='homee'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
]