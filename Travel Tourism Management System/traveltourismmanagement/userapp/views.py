

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Users

def home(request):
    return render(request,"base.html")

def user_login(request):
    if request.user.is_authenticated:
        redirect("/")
    else:
        if request.method == "POST":
            pass
    return render(request, "user_login.html")

def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        gender = request.POST['gender']
        img = request.FILES['image']
        mobile = request.POST['phone']
        if password1 != password2:
            messages.error(request,"Passwords does not match")
            return redirect('user_signup')

        user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
        users = Users.objects.create(user_id=user,mobile=mobile,gender=gender,img=img)

        user.save()
        users.save()
        return redirect('user_login')

    return render(request,"user_signup.html")