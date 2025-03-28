from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),  # New dashboard route
    path('products/', views.products, name='products'),
    path('green-energy/', views.green_energy, name='green_energy'),
    path('booking/', views.booking, name='booking'),
    path('carbon-calculator/', views.carbon_calculator, name='carbon_calculator'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
