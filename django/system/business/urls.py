from django.urls import path
from system.business import views


urlpatterns = [
       
    path('business/', views.business, name="clients"),
    
]