from django.urls import path
from system.employees import views


urlpatterns = [
       
    path('employees/', views.employees, name="employees"),
 
]