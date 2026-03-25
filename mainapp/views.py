
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pswd')
        try:
            user = User.objects.get(email=email)
            user_auth = authenticate(request, username=user.username, password=password)
            if user_auth:
                login(request, user_auth)
                messages.success(request, 'Login successful!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
        except User.DoesNotExist:
            messages.error(request, 'User not found')
        return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('txt')
        email = request.POST.get('email')
        password = request.POST.get('pswd')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('signup')
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('index')

def ml(request):
    return render(request, 'ml.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def ai(request):
    return render(request, 'ai.html')

def project(request):
    return render(request, 'project.html')
