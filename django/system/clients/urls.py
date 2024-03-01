# IMPORT REQUIREMENTS
from django.urls import path
from system.clients import views
from system.clients import actions



urlpatterns = [
       

    path('clients/', views.clients, name="clients"),
    path('client/register/', views.client_register, name="client_register"),
    path('client/<token>', views.client_show, name="client_show"),
    path('client/edit/<token>', views.client_edit, name="client_edit"),
    path('client/delete/<token>', views.client_delete, name="client_delete"),

    path('client/create/', actions.client_create, name="client_create"),
    path('client/edit/update/<token>', actions.client_update, name="client_update"),
    path('client/photo/delete/<token>', actions.photo_delete, name="photo_delete"),
    path('client/profile/delete/<token>', actions.client_delete, name="profile_delete")
    
    
]