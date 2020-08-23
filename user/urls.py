from django.urls import path, include 
from django.conf import settings 
from . import views 
from django.conf.urls.static import static 
from .views import list_view

urlpatterns = [ 
		path('', views.index, name ='index'), 
		path('list_view/', list_view), 
] 
