from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . forms import LoginForm
from .forms import MyPasswordReset

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
    path('category-title/<val>', views.CategoryTitle.as_view(), name="category-title"),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name="product-detail"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('address/', views.address, name="address"),
    path('updateaddress/<int:pk>', views.updateaddress.as_view(), name="updateaddress"),
    
    path('addtocart/', views.addtocart, name="addtocart"),
    path('cart/', views.cart, name="cart"),
    
    path('checkout/', views.checkout, name="checkout"),
    path('pluscart/', views.plus_cart, name="pluscart"),
    path('minuscart/', views.minus_cart, name="minuscart"),
    path('removecart/', views.remove_cart, name='removecart'),
    path('cart/update/<int:pk>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),


    
    # login authentication
    
    path('registration/', views.CustomerRegistrationView.as_view(), name="registration"),
     
    path('login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name="login"),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name="logout"),
    path('passwordreset/', auth_view.PasswordResetView.as_view(template_name='passwordreset.html', form_class=MyPasswordReset), name="passwordreset"),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
