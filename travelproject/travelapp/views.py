from django.contrib import messages, auth
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from requests import auth


# Create your views here.
def home(request):
    return render(request,'home.html')
def tem(request):
    return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get(
            'username')  # username enna variablelek login.html le name aya username fetch cheyth eduknu
        password = request.POST.get('password')  # password enna variablelekum fetch cheyth eduthu
        user = authenticate(username=username,
                                 password=password)  # db il ulla username um password um nammal thott mukalil store cheythvach password um username umkoduthatum same anonn authenticate cheyth nokkunnnu
        #
        if user is not None:
            auth_login(request, user)
            messages.info(request, "success login")
            return redirect('tem')
        else:
            messages.info(request, "invalid username or password")
            return redirect('login')
    #
    return render(request, 'login.html')


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save();
                messages.info(request, "user created")
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')

    return render(request, 'register.html')


def logout(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')