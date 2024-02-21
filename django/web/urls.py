from django.urls import path
from web import views


urlpatterns = [
    
    path('', views.index, name="site_index"),
    path('contact/', views.contact, name="site_contact"),
    
]