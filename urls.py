from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('green-energy/', views.green_energy, name='green_energy'),
    path('services/', views.services, name='services'),
    path('carbon-calculator/', views.carbon_calculator, name='carbon_calculator'),
    path('contact/', views.contact, name='contact'),
]
