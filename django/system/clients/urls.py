from django.urls import path
from system.clients import views


urlpatterns = [
       
    path('clients/', views.clients, name="clients"),
    path('client/register/', views.client_register, name="client_register"),
    path('client/<id>', views.client_show, name="client_show"),
    path('client/edit/<id>', views.client_edit, name="client_edit"),
    path('client/photo/delete/<id>', views.photo_delete, name="photo_delete"),
    path('client/delete/<id>', views.client_delete, name="client_delete"),
    
]