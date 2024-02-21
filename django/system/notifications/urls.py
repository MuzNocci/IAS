from django.urls import path
from system.notifications import views


urlpatterns = [

    path('notifications/', views.notifications, name="notifications"),

]