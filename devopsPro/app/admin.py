from django.contrib import admin
from . models import Product, Customer, Cart

# Register your models here.

@admin.register(Product)
class ProductionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'mobile', 'locality', 'city', 'zipcode', 'state'] 
    list_filter = ['state', 'city']

@admin.register(Cart)
class CartrModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity'] 
    
    
