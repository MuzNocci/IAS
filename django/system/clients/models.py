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
    

### TABELA :: CLIENTS
class Clients(models.Model):

    business = models.IntegerField(validators=[MaxValueValidator(99999999999)], blank=False, null=False)
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
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    birthday = models.CharField(max_length=10, blank=True, null=True)
    observation = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=9, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    number_address = models.CharField(max_length=5, blank=True, null=True)
    complement_address = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    icms_exempt = models.BooleanField(default=False)
    simple_tax = models.BooleanField(default=False)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> int:
        return self.id