# IMPORT REQUIREMENTS
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from authentication.utils import remove_char
# IMPORT MODELS
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

    if request.session.get('alert', False):

        data = request.session['data']
        type_alert = request.session['type_alert'] 
        alert = request.session['alert']
        del(request.session['data'])
        del(request.session['type_alert'])
        del(request.session['alert'])

    else:

        data = ''
        type_alert = ''
        alert = ''
     
    context = {
        'logged_user':logged_user,
        'logged_data':logged_userdata,

        'data':data,
        'type_alert': type_alert,
        'alert': alert,
    }
    return render(request, 'client_register.html', context)



# PAGE - CLIENT SHOW
@login_required
def client_show(request, token):

    logged_user = User.objects.get(username=request.user)
    logged_userdata = Userdata.objects.get(email=request.user)
    client = Clients.objects.get(token=token, business=logged_userdata.business)

    birthday_treated = client.birthday[8:10]+'/'+client.birthday[5:7]+'/'+client.birthday[0:4]
    sex_treated = 'Feminino' if client.sex == 'F' else ('Masculino' if client.sex == 'M' else 'Outro')
    phone_treated = remove_char(client.phone,'() -')
    created_at = str(client.created_at)
    created_at_date = created_at[8:10]+'/'+created_at[5:7]+'/'+created_at[0:4]
    created_at_hour = created_at[11:13]+':'+created_at[14:16]+':'+created_at[17:19]
    updated_at = str(client.updated_at)
    updated_at_date = updated_at[8:10]+'/'+updated_at[5:7]+'/'+updated_at[0:4]
    updated_at_hour = updated_at[11:13]+':'+updated_at[14:16]+':'+updated_at[17:19]

    context = {
        'logged_user':logged_user,
        'logged_data':logged_userdata,
        'client':client,
        'birthday_treated':birthday_treated,
        'phone_treated':phone_treated,
        'sex_treated':sex_treated,
        'created_at_date':created_at_date,
        'created_at_hour':created_at_hour,
        'updated_at_date':updated_at_date,
        'updated_at_hour':updated_at_hour,
    }
    return render(request, 'client_show.html', context)



# PAGE - CLIENT EDIT
@login_required
def client_edit(request, token):

    logged_user = User.objects.get(username=request.user)
    logged_userdata = Userdata.objects.get(email=request.user)
    client = Clients.objects.get(token=token, business=logged_userdata.business)

    context = {
        'logged_user':logged_user,
        'logged_data':logged_userdata,
        'client':client,
    }
    return render(request, 'client_edit.html', context)



# PAGE - CLIENT DELETE
@login_required
def client_delete(request, token):
    
    logged_user = User.objects.get(username=request.user)
    logged_userdata = Userdata.objects.get(email=request.user)
    client = Clients.objects.get(token=token, business=logged_userdata.business)

    if request.method == 'POST':

        alert = {}
        
        context = {
            'logged_user':logged_user,
            'logged_data':logged_userdata,
            'client':client,
            'alert':alert,
        }
        return render(request, 'client_delete.html', context)
    
    else:

        context = {
            'logged_user':logged_user,
            'logged_data':logged_userdata,
            'client':client,
        }
        return render(request, 'client_delete.html', context)