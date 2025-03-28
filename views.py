from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import Profile
from .models import Product
from .forms import ContactForm

def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically create a profile linked to the new user
            Profile.objects.create(user=user, firstname=user.username, lastname="Not provided", email=user.email)
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('dashboard')  # Redirect to dashboard after login
            else:
                messages.error(request, 'Invalid credentials.')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

@login_required
def dashboard(request):
    username = request.user.username  # Get the logged-in user's username
    return render(request, 'dashboard.html', {'username': username})

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def green_energy(request):
    return render(request, 'green_energy.html')

def booking(request):
    return render(request, 'booking.html')

def carbon_calculator(request):
    return render(request, 'carbon_calculator.html')

def contact(request):
    success_message = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Thank you! Your message has been sent successfully."
            form = ContactForm()  # Clear the form after submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'success_message': success_message})

