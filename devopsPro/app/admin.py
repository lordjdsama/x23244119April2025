"""Admin configuration for Product, Customer, and Cart models."""

from django.contrib import admin
from .models import Product, Customer, Cart

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    """Admin configuration for the Product model."""
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    """Admin configuration for the Customer model."""
    list_display = ['id', 'user', 'name', 'mobile', 'locality', 'city', 'zipcode', 'state']
    list_filter = ['state', 'city']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    """Admin configuration for the Cart model."""
    list_display = ['id', 'user', 'product', 'quantity']
