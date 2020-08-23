from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import GeeksModel



class UserRegisterForm(UserCreationForm): 
	email = forms.EmailField() 
	phone_no = forms.CharField(max_length = 20) 
	first_name = forms.CharField(max_length = 20) 
	last_name = forms.CharField(max_length = 20) 
	class Meta: 
		model = User 
		fields = ['username', 'email', 'phone_no', 'password1', 'password2'] 

class GeeksForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = GeeksModel 
  
        # specify fields to be used 
        fields = [ 
            "title", 
            "description", 
        ] 