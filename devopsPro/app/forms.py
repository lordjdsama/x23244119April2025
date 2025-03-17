from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from . models import Customer

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
   
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password','class': 'form-control'}))
    
class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
   
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  

       
        
        if commit:
            user.save()
        return user

class MyPasswordReset(PasswordResetForm):
    pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'name', 'locality', 'city','mobile' , 'state', 'zipcode']
        widgets = {
            'name' :forms.TextInput(attrs={'class': 'form-control'}),
            'locality' :forms.TextInput(attrs={'class': 'form-control'}),
            'city' :forms.TextInput(attrs={'class': 'form-control'}),
            'mobile' :forms.NumberInput(attrs={'class': 'form-control'}),
            'state' :forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode' :forms.TextInput(attrs={'class': 'form-control'}),
        }