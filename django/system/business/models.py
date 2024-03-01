# IMPORT REQUIREMENTS
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone



STATE_CHOICES = (
    ('AC', 'Acre'), 
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)
    

class Business(models.Model):
    
    token = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=254, blank=True, null=True) # RAZÃO SOCIAL
    surname = models.CharField(max_length=45, blank=False, null=False) # NOME FANTASIA
    register = models.CharField(max_length=18, unique=True, blank=True, null=True) # CNPJ
    enrollment_s = models.CharField(max_length=15, unique=True, blank=True, null=True) # INSCRIÇÃO ESTADUAL
    enrollment_c = models.CharField(max_length=15, unique=True, blank=True, null=True) # INSCRIÇÃO MUNICIPAL
    email = models.CharField(max_length=150, unique=True, blank=True, null=True)
    phone1 = models.CharField(max_length=13, blank=True, null=True)
    phone2 = models.CharField(max_length=13, blank=True, null=True)
    cellphone = models.CharField(max_length=14, blank=True, null=True)
    observation = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=9, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    number_address = models.CharField(max_length=5, blank=True, null=True)
    complement_address = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=254, blank=True, null=True)
    logo_sm = models.CharField(max_length=254, blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.token