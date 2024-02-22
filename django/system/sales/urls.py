from django.urls import path
from system.sales import views


urlpatterns = [
       
    path('sales/', views.sales, name="sales"),
 
]