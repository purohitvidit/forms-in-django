from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def green_energy(request):
    return render(request, 'green_energy.html')

def services(request):
    return render(request, 'services.html')

def carbon_calculator(request):
    return render(request, 'carbon_calculator.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')


