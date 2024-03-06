from django.http import HttpResponse
from django.shortcuts import render
from .forms import CoffeePaymentForms
import razorpay
from .models import ColdCoffee
# Create your views here.

def coffeepayment(request):
    if request.method == "POST":
        name = request.POST['name']
        amount = int(request.POST['amount'])*100

        client = razorpay.Client(auth=("rzp_test_PGANogrOpwY11W","LsbcZFInV3DIAzMPHwM3iOYZ"))


        response_payment = client.order.create(dict(
            amount = amount,
            currency ="INR"
        ))
        order_id = response_payment['id']
        order_status = response_payment['status']
        if response_payment['status'] == "created":
            coffee = ColdCoffee(name=name, amount=amount, order_id=order_id)
            coffee.save()
            response_payment['name'] = name

        # print(response_payment)
        form = CoffeePaymentForms(request.POST or None)
        return render(request,"coffee_payment.html",{'form':form,"payment":response_payment})

    form = CoffeePaymentForms()
    return render(request,'coffee_payment.html',{'form':form})

def paymentstatus(request):
    response =request.POST
    print(response)
    return HttpResponse("OK")
    #retun render(request,"payment-status.html")

