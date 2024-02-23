from django.urls import path
from system.clients import views
from system.clients import actions


urlpatterns = [
       
    # PAGES
    path('clients/', views.clients, name="clients"),
    path('client/register/', views.client_register, name="client_register"),
    path('client/<id>', views.client_show, name="client_show"),
    path('client/edit/<id>', views.client_edit, name="client_edit"),
    path('client/delete/<id>', views.client_delete, name="client_delete"),

    # ACTIONS
    path('client/create/', actions.client_create, name="client_create"),
    path('client/edit/update/<id>', actions.client_update, name="client_update"),
    path('client/photo/delete/<id>', actions.photo_delete, name="photo_delete"),
    path('client/profile/delete/<id>', actions.client_delete, name="profile_delete")
    
]