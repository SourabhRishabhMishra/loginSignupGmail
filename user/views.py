from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm 
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 
#import datetime
#from django.http import HttpResponse
from .models import GeeksModel
from django.views.generic.list import ListView
from .forms import GeeksForm
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

#################### index####################################### 
def index(request): 
	return render(request, 'user/index.html', {'title':'index'}) 

########### register here ##################################### 
def register(request): 
	if request.method == 'POST': 
		form = UserRegisterForm(request.POST) 
		if form.is_valid(): 
			form.save() 
			username = form.cleaned_data.get('username') 
			email = form.cleaned_data.get('email') 
			######################### mail system #################################### 
			htmly = get_template('user/Email.html') 
			d = { 'username': username } 
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email 
			html_content = htmly.render(d) 
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
			msg.attach_alternative(html_content, "text/html") 
			msg.send() 
			################################################################## 
			messages.success(request, f'Your account has been created ! You are now able to log in') 
			return redirect('login') 
	else: 
		form = UserRegisterForm() 
	return render(request, 'user/register.html', {'form': form, 'title':'reqister here'}) 

################ login forms################################################### 
def Login(request): 
	if request.method == 'POST': 

		# AuthenticationForm_can_also_be_used__ 

		username = request.POST['username'] 
		password = request.POST['password'] 
		user = authenticate(request, username = username, password = password) 
		if user is not None: 
			form = login(request, user) 
			messages.success(request, f' wecome {username} !!') 
			return redirect('index') 
		else: 
			messages.info(request, f'account done not exit plz sign in') 
	form = AuthenticationForm() 
	return render(request, 'user/login.html', {'form':form, 'title':'log in'}) 

class GeeksList(ListView): 
  
    # specify the model for list view 
    model = GeeksModel 

def create_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    form = GeeksForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
          
    context['form']= form 
    return render(request, "user/create_view.html", context)

def list_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = GeeksModel.objects.all() 
          
    return render(request, "user/list_view.html", context) 

def detail_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["data"] = GeeksModel.objects.get(id = id)
          
    return render(request, "user/detail_view.html", context)

# update view for details 
def update_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(GeeksModel, id = id) 
  
    # pass the object as instance in form 
    form = GeeksForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 	
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id) 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "user/update_view.html", context) 

def delete_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(GeeksModel, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/") 
  
    return render(request, "user/delete.html", context)