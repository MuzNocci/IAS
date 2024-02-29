from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authentication.models import Userdata


@login_required
def business(request):
    
    logged_user = User.objects.get(username=request.user)
    logged_userdata = Userdata.objects.get(email=request.user)
    
    context = {
        'logged_user':logged_user,
        'logged_data':logged_userdata
    }
    return render(request, 'business.html', context)