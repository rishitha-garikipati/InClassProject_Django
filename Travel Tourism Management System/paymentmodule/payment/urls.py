from django.urls import path
from .import views
urlpatterns =[
    path("",views.coffeepayment,name='coffee-payment'),
    path('payment-status',views.paymentstatus,name='payment-status')
]