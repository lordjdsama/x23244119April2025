from django.db.models import Count
from urllib import request
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from . models import Product, Customer
from . forms import CustomerRegistrationForm, ProfileForm
from django.contrib import messages

# Create your views here.
def home (request):
    return render(request, "index.html")
def about (request):
    return render(request, "about.html")
def contact (request):
    return render(request, "contact.html")
    

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "category.html", locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')  
        return render(request, "category.html", locals())
        
class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "productdetail.html", {'product': product, 'pk': pk})  
  
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "customerregistration.html", locals())  
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Registration Successful")
        else:
            messages.warning(request,"Invalid Input")
        return render(request, "customerregistration.html", locals())
        
        
class ProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'profile.html', locals())
    def post(self,request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user, name=name, city=city,locality=locality,mobile=mobile, state=state,zipcode=zipcode)
            reg.save()
            messages.success(request, "Profile Saved")
        else:
            messages.warning(request, "Invalid Data")
        return render(request, 'profile.html', locals())
        

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', locals())
    
    
class updateaddress(View):
      def get(self, request):
        form = ProfileForm()
        return render(request, 'updateaddress.html', locals())
      def post(self,request):
        form = ProfileForm(request.POST)
        return render(request, 'updateaddress.html', locals())
     