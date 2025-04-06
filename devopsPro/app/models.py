"""
Models for the app: Product, Customer, Cart.
"""

from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('ST', 'String'),
    ('RT', 'Rhythm'),
    ('VO', 'Vocal'),
    ('PR', 'Production'),
    ('CO', 'Composition'),
    ('MG', 'Management'),
)


class Product(models.Model):
    """
    Represents a product/course in the platform.
    """
    title = models.CharField(max_length=100)
    course_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    career_in = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return str(self.title)


class Customer(models.Model):
    """
    Stores customer profile information.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    city = models.CharField(default="", max_length=200)
    locality = models.CharField(max_length=200)
    mobile = models.IntegerField()
    zipcode = models.IntegerField()
    state = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Cart(models.Model):
    """
    Shopping cart storing user-selected products and quantities.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        """
        Calculates total cost based on quantity and discounted price.
        """
        return self.quantity * self.product.discounted_price
