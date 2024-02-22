from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authentication.models import Userdata


@login_required
def employees(request):
    pass