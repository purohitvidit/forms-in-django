from django.contrib import admin
from .models import Profile
from .models import Product
from .models import Contact
# Register your models here.

admin.site.register(Profile)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')