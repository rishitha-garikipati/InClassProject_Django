from django.shortcuts import render, redirect
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as lg



# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        gender = request.POST['gender']
        mobile = request.POST['phone']

        if password1 != password2:
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                         last_name=last_name, email=email)
        user.save()
        user_profile = Users.objects.create(user_id=user, gender=gender, mobile=mobile)
        user_profile.save()

        # Redirect to login page upon successful signup
        return redirect('login')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if len(username) == username:
                lg(request, user)
                return redirect('home')
        else:
            return render(request, 'login.html', {'fail': True})
    else:
        return render(request, 'login.html', {'fail': False})

def homee(request):
    return render(request,'homee.html')