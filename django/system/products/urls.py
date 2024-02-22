from django.urls import path
from system.products import views


urlpatterns = [
       
    path('products/', views.products, name="products"),
 
]