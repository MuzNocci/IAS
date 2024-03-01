# IMPORT REQUIREMENTS
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone



SEX_CHOICES = (
    ('M','Masculino'),
    ('F','Feminino'),
    ('O','Outro'),
)

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


class Userdata(models.Model):
    

    email = models.CharField(max_length=150, unique=True, blank=False, null=False)
    email_marketing = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    photo = models.CharField(max_length=255, blank=True, null=True)
    register = models.CharField(max_length=14, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    zipcode = models.CharField(max_length=9, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    number_address = models.CharField(max_length=5, blank=True, null=True)
    address_component = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(validators=[MaxValueValidator(99)], blank=True, null=True) # Criar relacionamento
    business = models.CharField(max_length=16, blank=True, null=True)
    plan = models.IntegerField(validators=[MaxValueValidator(99)], blank=True, null=True) # Criar relacionamento
    plan_expire = models.DateField(blank=True, null=True)
    remember_token = models.CharField(max_length=128, unique=True, blank=False, null=True)
    created_by = models.CharField(max_length=255, unique=True, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.CharField(max_length=255, unique=True, blank=False)
    updated_at = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self) -> int:
        return super().id