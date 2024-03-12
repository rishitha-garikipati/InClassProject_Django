from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import CoffeePaymentForm
from .models import ColdCoffee
import razorpay

# Create your views here.

def coffeepayment(request):
    if request.method == "POST":
        name = request.POST['name']
        amount = int(request.POST['amount'])*100

        # create razorpay client
        client = razorpay.Client(auth=("rzp_test_PGANogrOpwY11W","LsbcZFInV3DIAzMPHwM3iOYZ"))

        # create order
        response_payment = client.order.create(dict(
            amount = amount,
            currency = "INR"
        ))
        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == "created":
            coffee = ColdCoffee(name=name,amount=amount,order_id=order_id)
            coffee.save()
            response_payment['name'] = name
            # print(response_payment)
            form = CoffeePaymentForm(request.POST or None)
            return render(request, "coffee_payment.html", {'form': form, "payment": response_payment})

    form = CoffeePaymentForm()
    return render(request,'coffee_payment.html',{'form':form})

@csrf_exempt
def paymentstatus(request):
     response1 = request.POST
     params_dict = {
        "razorpay_payment_id": response1["razorpay_payment_id"],
        "razorpay_order_id": response1["razorpay_order_id"],
        "razorpay_signature": response1["razorpay_signature"]
     }
     # create razorpay client
     client = razorpay.Client(auth=("rzp_test_PGANogrOpwY11W","LsbcZFInV3DIAzMPHwM3iOYZ"))

     try:
         status = client.utility.verify_payment_signature(params_dict)
         coldcoffee = ColdCoffee.objects.get(order_id = response1['razorpay_order_id'])
         coldcoffee.razorpay_payment_id = response1['razorpay_payment_id']
         coldcoffee.paid = True
         coldcoffee.save()
         return render(request,'payment_status.html',{'status': True})
     except:
         return render(request,'payment_status.html',{'status': False})