from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username= username, password=password)

        if user is not None:
            auth.login(request,user)
            
            return redirect('questions')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect( '/')
    
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method== 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']
        

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already Used')           
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register') 
            
            else:
                user = User.objects.create_user(username=username, email=email, password= password)
                user.save(); ######## I DON'T SEE THE POINT OF THE ; USED HERE
                return redirect('login')
        else:
            messages.info(request, 'Password confirmation failed')
            return redirect('register')
    else:
        return render(request, 'login.html')

def questions(request):
    return render(request, 'Audition Form.html')
