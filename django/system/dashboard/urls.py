from django.urls import path
from system.dashboard import views


urlpatterns = [
       
    path('dashboard/', views.dashboard, name="dashboard"),
 
]