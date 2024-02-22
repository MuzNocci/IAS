from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    
    # Site
    path('', include('web.urls')),
    
    # Administração
    # path('auth/administrator/system/', admin.site.urls),
    
    # Authentication
    path('auth/', include('authentication.urls')),
    
    # Sistema
    path('auth/', include('system.business.urls')),
    path('auth/', include('system.clients.urls')),
    path('auth/', include('system.dashboard.urls')),
    path('auth/', include('system.employees.urls')),
    path('auth/', include('system.notifications.urls')),
    path('auth/', include('system.products.urls')),
    path('auth/', include('system.profiles.urls')),
    
]