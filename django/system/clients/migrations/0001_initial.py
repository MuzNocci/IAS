# Generated by Django 5.0.1 on 2024-02-29 13:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True)),
                ('business', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=254)),
                ('register', models.CharField(blank=True, max_length=14, null=True)),
                ('surname', models.CharField(blank=True, max_length=254, null=True)),
                ('registration', models.CharField(blank=True, max_length=18, null=True)),
                ('sector', models.CharField(blank=True, max_length=45, null=True)),
                ('jobposition', models.CharField(blank=True, max_length=45, null=True)),
                ('photo', models.CharField(blank=True, max_length=254, null=True)),
                ('email', models.CharField(max_length=150)),
                ('email_marketing', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('whatsapp', models.BooleanField(default=False)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, null=True)),
                ('birthday', models.CharField(blank=True, max_length=10, null=True)),
                ('observation', models.TextField(blank=True, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=9, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('number_address', models.CharField(blank=True, max_length=5, null=True)),
                ('complement_address', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=45, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('state', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('icms_exempt', models.BooleanField(default=False)),
                ('simple_tax', models.BooleanField(default=False)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
