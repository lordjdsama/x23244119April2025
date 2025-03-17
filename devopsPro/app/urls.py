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
    path('updateaddress/', views.updateaddress.as_view(), name="updateaddress"),
    
    # login authentication
    
    path('registration/', views.CustomerRegistrationView.as_view(), name="registration"),
     
    path('login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name="login"),
    
    path('passwordreset/', auth_view.PasswordResetView.as_view(template_name='passwordreset.html', form_class=MyPasswordReset), name="passwordreset"),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
