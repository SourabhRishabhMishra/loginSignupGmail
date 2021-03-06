from django.urls import path, include 
from django.conf import settings 
from . import views 
from django.conf.urls.static import static 
#from .views import list_view
from .views import GeeksList

urlpatterns = [ 
		path('', views.index, name ='index'), 
		path('list_view/', GeeksList.as_view()), 
		path('create_view/', views.create_view), 
		path('list_view/', views.list_view), 
		path('<id>', views.detail_view ),
		path('<id>/update', views.update_view),
		path('<id>/delete', views.delete_view),
] 
