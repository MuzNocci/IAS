# IMPORT REQUIREMENTS
from django.db import models
from django.utils import timezone



class Clients(models.Model):


    token = models.CharField(max_length=64, unique=True)
    business = models.CharField(max_length=16, blank=False, null=False)
    name = models.CharField(max_length=254, blank=False, null=False)
    register = models.CharField(max_length=14, blank=True, null=True)
    surname = models.CharField(max_length=254, blank=True, null=True)
    registration = models.CharField(max_length=18, blank=True, null=True)
    sector = models.CharField(max_length=45, blank=True, null=True)
    jobposition = models.CharField(max_length=45, blank=True, null=True)
    photo = models.CharField(max_length=254, blank=True, null=True)
    email = models.CharField(max_length=150, blank=False)
    email_marketing = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.BooleanField(default=False)
    genre = models.CharField(max_length=1, blank=True, null=True)
    birthday = models.CharField(max_length=10, blank=True, null=True)
    observation = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=9, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    number_address = models.CharField(max_length=5, blank=True, null=True)
    complement_address = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    icms_exempt = models.BooleanField(default=False)
    simple_tax = models.BooleanField(default=False)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    

    def __str__(self) -> int:
        return self.id