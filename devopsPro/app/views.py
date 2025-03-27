from django.db.models import Count, Q
from urllib import request
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from . models import Product, Customer, Cart
from . forms import CustomerRegistrationForm, ProfileForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



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
    def get(self, request, *args, **kwargs): 
        pk = kwargs.get('pk')
        add = get_object_or_404(Customer, pk=pk) 
        form = ProfileForm(instance=add)  
        return render(request, 'updateaddress.html', {'form': form, 'add': add})  

    def post(self, request, *args, **kwargs): 
        pk = kwargs.get('pk')
        add = get_object_or_404(Customer, pk=pk) 
        form = ProfileForm(request.POST, instance=add)

        if form.is_valid():
            form.save()  
            messages.success(request, "Address Updated Successfully")
            return redirect('address')  

        messages.warning(request, "Invalid Input")
        return render(request, 'updateaddress.html', {'form': form, 'add': add})  



def addtocart(request):
    user = request.user
    productid = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=productid)  # ✅ Prevent errors
    Cart(user=user, product=product).save()
    return redirect("cart")  # ✅ Redirect to cart page

def cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    
    return render(request, 'addtocart.html', locals())
    
def checkout(request):
    return render(request, 'checkout.html', locals())
    
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
            
        }
        return JsonResponse(data)
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        
        if c.quantity > 1:
            c.quantity -= 1
            c.save()
        
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = sum(item.quantity * item.product.discounted_price for item in cart)
        totalamount = amount + 40

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()

        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = sum(item.quantity * item.product.discounted_price for item in cart)
        totalamount = amount + 40 if amount > 0 else 0

        data = {
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
 
def update_cart_quantity(request, pk, action):
    cart_item = get_object_or_404(Cart, pk=pk, user=request.user)

    if action == 'increase':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
    elif action == 'remove':
        cart_item.delete()

    return redirect('cart')