from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('ST', 'String'),
    ('RT', 'Rhytym'),
    ('VO', 'Vocal'),
    ('PR', 'Prodution'),
    ('CO', 'Composition'),
    ('MG', 'Management'),
    
    )

class Product(models.Model):
    title = models.CharField(max_length=100)
    course_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    career_in = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
        
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    city = models.CharField(default="",max_length=200)
    locality = models.CharField(max_length=200)
    mobile = models.IntegerField()
    zipcode = models.IntegerField()
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    