import os
from datetime import date, time
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from PIL import Image
from core.settings import BASE_DIR
from authentication.utils import valid_file, valid_cpf, valid_mail, remove_char
from django.utils import timezone


# Import Models
from django.contrib.auth.models import User
from authentication.models import Userdata
from system.clients.models import Clients



@login_required(login_url='/auth/signin')
def clients(request):
    
    user = User.objects.get(username=request.user)
    userdata = Userdata.objects.get(email=request.user)

    if request.session.get('alert', False):
        type_alert = request.session['type_alert']
        alert = request.session['alert']
        del(request.session['type_alert'])
        del(request.session['alert'])
    else:
        type_alert = ''
        alert = ''
    
    # SEARCH
    search = request.GET.get("search", "")
    if search:
        clients = Clients.objects.filter(Q(business=userdata.business) & Q(name__icontains=search) | Q(surname__icontains=search) | Q(email__icontains=search)).order_by('name')
    else:
        clients = Clients.objects.filter(business=userdata.business).order_by('name')
    
    # PAGINATION
    show_number = request.GET.get("show", 10)
    page_number = request.GET.get('page', 1)
    
    paginator = Paginator(clients, show_number)
    pages = paginator.page(page_number)

    context = {
        
        'logged_user':user,
        'logged_data':userdata,
        
        'clients':clients,
        'search':search,
        'show':show_number,
        'pages':pages,
        
        'type_alert': type_alert,
        'alert': alert,

    }
    return render(request, 'clients.html', context)


# PAGE - CLIENT REGISTER
@login_required(login_url='/auth/signin')
def client_register(request):
    
    logged_user = User.objects.get(username=request.user)
    logged_userdata = Userdata.objects.get(email=request.user)
     
    if request.method == 'POST':
        
        alert = []
        
        photo = request.FILES.get('photo', "")
        client_photo = ''
        if photo != '':
            if valid_file(photo.name) == 'jpg' or valid_file(photo.name) == 'png' or valid_file(photo.name) == 'svg'  or valid_file(photo.name) == 'jpeg':
                image = Image.open(photo)
                client_photo = f'{photo.name.replace(f'.{valid_file(photo.name)}', '')}_{request.user.id}.{valid_file(photo.name)}'
                
                if not os.path.isdir(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/')):
                    os.makedirs(os.path.join(BASE_DIR,f'static/system/images/customers/{logged_userdata.business}/'))
                
                image.save(os.path.join(BASE_DIR, f'static/system/images/customers/{logged_userdata.business}/{client_photo}'))
            else:
                alert.append('- Imagem inválida.')
        
        client_name = request.POST.get('name', "")
        client_register = request.POST.get('cpf', "") 
        client_sex = request.POST.get('sex', "")
        client_birthday = request.POST.get('birthday', '0000-00-00')
        client_email = request.POST.get('email', "")
        client_email_marketing = request.POST.get('email_marketing', 0)
        client_phone = request.POST.get('phone', "")
        client_email = request.POST.get('email', "")
        client_whatsapp = request.POST.get('whatsapp', 0)
        client_surname = request.POST.get('surname', "")
        client_registration = request.POST.get('registration', "")
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
        
        if len(alert) != 0:
            
            context = {
                'logged_user':logged_user,
                'logged_data':logged_userdata,
                
                'type_alert':'alert-danger',
                'alert':alert, 
            }
            return render(request, 'client_register.html', context)
            
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
                created_by = logged_user.first_name +' '+ logged_user.last_name,
            )
            new_client.save()
        
            request.session['type_alert'] = 'alert-success'
            request.session['alert'] = 'Cliente cadastrado!'
            
            return redirect('clients')

    context = {
        'logged_user':logged_user,
        'logged_data':logged_userdata
    }
    return render(request, 'client_register.html', context)


# PAGE - CLIENT SHOW
def client_show(request, id=0):

    logged_user = User.objects.get(username=request.user)
    logged_userdata = Userdata.objects.get(email=request.user)

    client = Clients.objects.get(id=id, business=logged_userdata.business)

    birthday_treated = client.birthday[8:10]+'/'+client.birthday[5:7]+'/'+client.birthday[0:4]
    sex_treated = 'Feminino' if client.sex == 'F' else ('Masculino' if client.sex == 'M' else 'Outro')
    phone_treated = remove_char(client.phone,'() -')

    context = {
        'logged_user':logged_user,
        'logged_data':logged_userdata,
        'client':client,
        'birthday_treated':birthday_treated,
        'phone_treated':phone_treated,
        'sex_treated':sex_treated,
    }
    return render(request, 'client_show.html', context)