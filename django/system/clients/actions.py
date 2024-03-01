# IMPORT REQUIREMENTS
import os
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from PIL import Image
from core.settings import BASE_DIR
from authentication import validators
from authentication import utils
from django.utils import timezone
from django.utils.crypto import get_random_string
# IMPORT MODELS
from django.contrib.auth.models import User
from authentication.models import Userdata
from system.clients.models import Clients



@login_required
def client_create(request):


    if request.method == 'POST':

        logged_user = User.objects.get(username=request.user)
        logged_userdata = Userdata.objects.get(email=request.user)
        
        alert = {}

        photo = request.FILES.get('photo', "")
        client_photo = ''

        if photo != '':
            
            if validators.valid_type(photo.name, ['jpg','png','gif','svg','jpeg']):

                image = Image.open(photo)
                client_photo = f'{timezone.localtime(timezone.now()).strftime('%Y%m%dT%H%M%S')}00{request.user.id}.{utils.file_extension(photo.name)}'
                
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


        client_genre = request.POST.get('genre', "")


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

            request.session['data'] = request.POST
            request.session['type_alert'] = 'alert-danger'
            request.session['alert'] = alert

            return redirect('client_register')
            
        else:
            
            new_client = Clients(
                token = get_random_string(length=64),
                business = logged_userdata.business,
                photo = client_photo,
                name = client_name,
                register = client_register,
                genre = client_genre,
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



@login_required
def client_update(request, token):


    if request.method == 'POST':

        logged_user = User.objects.get(username=request.user)
        logged_userdata = Userdata.objects.get(email=request.user)
        client = Clients.objects.get(token=token, business=logged_userdata.business)

        alert = {}


        photo = request.FILES.get('photo', False)
        client_photo = ''
        
        if photo:

            if validators.valid_type(photo.name, ['jpg','png','gif','svg','jpeg']):
                
                image = Image.open(photo)
                client_photo = f'{timezone.localtime(timezone.now()).strftime('%Y%m%dT%H%M%S')}00{request.user.id}.{utils.file_extension(photo.name)}'
            
                if client.photo != '':
                    if os.path.isdir(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/{client.photo}')):
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


        client_register = request.POST.get('cpf', "") 

        if client_register != '':
            if not validators.valid_cpf(client_register):
                alert['register'] = '- CPF inválido.'


        client_genre = request.POST.get('genre', "")


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


        if len(alert) > 0:

            request.session['data'] = request.POST
            request.session['type_alert'] = 'alert-danger'
            request.session['alert'] = alert

            return HttpResponseRedirect(reverse('client_edit', kwargs={'token':client.token}))
        
        else:
        

            Clients.objects.filter(token=token, business=logged_userdata.business).update(

                photo = client_photo,
                name = client_name,
                register = client_register,
                genre = client_genre,
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
                updated_by=logged_user.first_name +' '+ logged_user.last_name,
                updated_at=timezone.now()

            )
            return HttpResponseRedirect(reverse('client_show', kwargs={'token':client.token}))



@login_required
def photo_delete(request, token):


    logged_userdata = Userdata.objects.get(email=request.user)
    client = Clients.objects.get(token=token, business=logged_userdata.business)


    try:
        os.remove(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/{client.photo}'))
    
    except:
        pass

    Clients.objects.filter(token=token).update(photo='')


    return HttpResponseRedirect(reverse('client_edit', kwargs={'token':client.token}))



@login_required
def client_delete(request, token):


    if request.method == 'POST':

        logged_userdata = Userdata.objects.get(email=request.user)
        client = Clients.objects.get(token=token, business=logged_userdata.business)


        try:
            os.remove(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/{client.photo}'))
        
        except:
            pass

        client.delete()


        request.session['type_alert'] = 'alert-success'
        request.session['alert'] = 'Cliente deletado!'

        return HttpResponseRedirect(reverse('clients'))
