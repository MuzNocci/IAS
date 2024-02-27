from django.urls import path
from authentication import views



urlpatterns = [

    # LOGIN SYSTEM
    # path('signup/', views.maintenance, name="signup"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('forgot/', views.forgot, name="forgot"),
    path('forgot/success/', views.forgot_success, name="forgot_success"),
    path('reset/', views.reset_password, name="reset_password"),
    path('signout/', views.signout, name="signout"),

]