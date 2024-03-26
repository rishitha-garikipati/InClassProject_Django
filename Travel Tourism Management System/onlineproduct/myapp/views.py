from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def home(request):
    return render(request,'home.html')
def addproduct(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        pname = request.POST.get('pname')
        price = request.POST.get('price')

        # Create a new Hotel object with the provided data
        product = Product.objects.create(
            pid=pid,
            pname=pname,
            price=price,
        )
        product.save()
        products = Product.objects.all()

        return render(request, 'addproduct.html', {'products': products})
    else:
        return render(request, 'addproduct.html')
