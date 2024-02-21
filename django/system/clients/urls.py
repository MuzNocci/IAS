from django.urls import path
from system.clients import views


urlpatterns = [
       
    path('clients/', views.clients, name="clients"),
    path('client/<id>', views.client_show, name="client_show"),
    path('client/register/', views.client_register, name="client_register"),
    
]