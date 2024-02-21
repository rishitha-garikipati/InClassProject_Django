from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import contactus
# Create your views here.
def home(request):
    return render(request,"home.html")
def weatherinfo(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'b0197d10a56c3ed637801d7b54edb0bb'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})
    return render(request,"weatherappinput.html")

def contactmail(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment + '-------------------- This is just the copy of comment what you have posted in MMS System'
        data = contactus(firstname=firstname, lastname=lastname, email=email, comments=comment)
        data.save()
        send_mail(
            'Thank You for Contacting Travel Tourism and Management  System',
            tosend,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Mail Sent</center></h1>")
        # return render(request, 'Homepage.html')
    else:
        HttpResponse("<h1>error</h1>")
    return render(request,'Contact.html')