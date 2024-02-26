import os
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from PIL import Image
from core.settings import BASE_DIR
from authentication import validators
from django.utils import timezone
from datetime import datetime


# Import Models
from django.contrib.auth.models import User
from authentication.models import Userdata
from system.clients.models import Clients


# PAGE - CLIENT CREATE
@login_required
def client_create(request):

    if request.method == 'POST':

        logged_user = User.objects.get(username=request.user)
        logged_userdata = Userdata.objects.get(email=request.user)
        
        alert = {}
        
        photo = request.FILES.get('photo', "")
        client_photo = ''
        if photo != '':
            if validators.valid_file(photo.name) == 'jpg' or validators.valid_file(photo.name) == 'png' or validators.valid_file(photo.name) == 'svg'  or validators.valid_file(photo.name) == 'jpeg':
                image = Image.open(photo)
                client_photo = f'{timezone.localtime(timezone.now()).strftime('%Y%m%dT%H%M%S')}00{request.user.id}.{validators.valid_file(photo.name)}'
                
                if not os.path.isdir(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/')):
                    os.makedirs(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/'))
            else:
                alert['photo'] = '- Imagem inválida.'
        
        client_name = request.POST.get('name')
        if not validators.valid_name(client_name):
            alert['name'] = '- Nome inválido.'


        client_register = request.POST.get('cpf', "") 
        if client_register != '':
            if not validators.valid_cpf(client_register):
                alert['register'] = '- CPF inválido.'

        client_sex = request.POST.get('sex', "")

        client_birthday = request.POST.get('birthday', '0000-00-00')
        if client_birthday != '':
            if not validators.valid_date(client_birthday):
                alert['birthday'] = '- Data de nascimento inválida.'

        client_email = request.POST.get('email', "")
        if client_email != '':
            if not validators.valid_mail(client_email):
                alert['email'] = '- E-mail inválido.'


        client_email_marketing = request.POST.get('email_marketing', 0)

        client_phone = request.POST.get('phone', "")
        if client_phone != '':
            if not validators.valid_phone(client_phone):
                alert['phone'] = '- Telefone inválido.'



        client_whatsapp = request.POST.get('whatsapp', 0)

        client_surname = request.POST.get('surname', "")
        if client_surname != '':
            if not validators.valid_name(client_surname):
                alert['surname'] = '- Nome inválido.'

        client_registration = request.POST.get('registration', "")
        if client_registration != '':
            if not validators.valid_cpf(client_registration):
                alert['CNPJ'] = '- CNPJ inválido.'

        client_sector = request.POST.get('sector', "")

        client_jobposition = request.POST.get('jobposition', 0)

        client_icms_exempt = request.POST.get('icms_exempt', 0)

        client_simple_tax = request.POST.get('simple_tax', "")

        client_zipcode = request.POST.get('zipcode', "")

        client_address = request.POST.get('address', "")

        client_number_address = request.POST.get('number_address', "")

        client_complement_address = request.POST.get('complement_address', "")

        client_district = request.POST.get('district', "")

        client_city = request.POST.get('city', "")

        client_state = request.POST.get('state', "")

        client_country = request.POST.get('country', "")
        
        client_observation = request.POST.get('observation', "")
        
        if len(alert) != 0:

            data = {
                'name':client_name,
                'register':client_register,
                'sex':client_sex,
                'birthday':client_birthday,
            }

            request.session['data'] = data
            request.session['type_alert'] = 'alert-danger'
            request.session['alert'] = alert

            return redirect('client_register')
            
        else:
            
            new_client = Clients(
                business = logged_userdata.business,
                photo = client_photo,
                name = client_name,
                register = client_register,
                sex = client_sex,
                birthday = client_birthday,
                email = client_email,
                email_marketing = client_email_marketing,
                phone = client_phone,
                whatsapp = client_whatsapp,
                surname = client_surname,
                registration = client_registration,
                sector = client_sector,
                jobposition = client_jobposition,
                icms_exempt = client_icms_exempt,
                simple_tax = client_simple_tax,
                zipcode = client_zipcode,
                address = client_address,
                number_address = client_number_address,
                complement_address = client_complement_address,
                district = client_district,
                city = client_city,
                state = client_state,
                country = client_country,
                observation = client_observation,
                created_by = logged_user.first_name +' '+ logged_user.last_name,
                updated_by = logged_user.first_name +' '+ logged_user.last_name,
            )
            new_client.save()

            if photo != '':
                image.save(os.path.join(BASE_DIR, f'static/system/images/customers/{logged_userdata.business}/{client_photo}'))
                
            request.session['type_alert'] = 'alert-success'
            request.session['alert'] = 'Cliente cadastrado!'
            
            return redirect('clients')


# PAGE - CLIENT UPDATE
@login_required
def client_update(request, id=0):

    if request.method == 'POST':

        logged_user = User.objects.get(username=request.user)
        logged_userdata = Userdata.objects.get(email=request.user)
        client = Clients.objects.get(id=id, business=logged_userdata.business)

        alert = {}

        photo = request.FILES.get('photo', False)
        client_photo = ''
        
        if photo:
            if validators.valid_file(photo.name) == 'jpg' or validators.valid_file(photo.name) == 'png' or validators.valid_file(photo.name) == 'svg'  or validators.valid_file(photo.name) == 'jpeg':
                
                image = Image.open(photo)
                client_photo = f'{timezone.localtime(timezone.now()).strftime('%Y%m%dT%H%M%S')}00{request.user.id}.{validators.valid_file(photo.name)}'
            
                if not os.path.isdir(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/{client.photo}')):
                    os.remove(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/{client.photo}'))
                
                if not os.path.isdir(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/')):
                    os.makedirs(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/'))
                
                image.save(os.path.join(BASE_DIR, f'static/system/images/customers/{logged_userdata.business}/{client_photo}'))
            
            else:

                alert['photo'] = '- Imagem inválida.'

        else:

            client_photo = client.photo

        client_name = request.POST.get('name')
        if not validators.valid_name(client_name):
            alert['name'] = '- Nome inválido.'

        client_register = request.POST.get('cpf') 
        if client_register != '':
            if not validators.valid_cpf(client_register):
                alert['cpf'] = '- CPF inválido.'

        client_birthday = request.POST.get('birthday', False)

        Clients.objects.filter(id=id).update(

            photo=client_photo,
            name=client_name,
            birthday=client_birthday,
            updated_by=logged_user.first_name +' '+ logged_user.last_name,
            updated_at=timezone.now()

        )
        return HttpResponseRedirect(reverse('client_show', kwargs={'id':client.id}))


# PAGE - PHOTO DELETE
@login_required
def photo_delete(request, id=0):

    logged_userdata = Userdata.objects.get(email=request.user)
    client = Clients.objects.get(id=id, business=logged_userdata.business)

    try:
        os.remove(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/{client.photo}'))
    except:
        pass

    Clients.objects.filter(id=id).update(photo='')

    return HttpResponseRedirect(reverse('client_edit', kwargs={'id':client.id}))


# PAGE - CLIENT DELETE
@login_required
def client_delete(request, id=0):

    if request.method == 'POST':

        logged_userdata = Userdata.objects.get(email=request.user)
        client = Clients.objects.get(id=id, business=logged_userdata.business)

        try:
            os.remove(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/{client.photo}'))
        except:
            pass

        client.delete()

        request.session['type_alert'] = 'alert-success'
        request.session['alert'] = 'Cliente deletado!'

        return HttpResponseRedirect(reverse('clients'))
