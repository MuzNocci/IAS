from django.urls import path
from system.profiles import views


urlpatterns = [
       
    path('profiles/', views.profiles, name="profiles"),
 
]