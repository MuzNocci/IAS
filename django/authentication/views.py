from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from authentication.validators import valid_cpf, valid_mail
# import Models
from django.contrib.auth.models import User
from authentication.models import Userdata
from system.business.models import Business



### PAGE - MAINTENANCE
def maintenance(request):
    return render(request, 'maintenance.html')


### SCRIPT - CREATE USER
@csrf_protect
def signup(request):
    
    # CREATE USER SCRIPT
    if request.method == 'POST':
        
        alert = []
        
        user_name = request.POST.get('name')
        user_register = request.POST.get('register')
        user_mail = request.POST.get('email')
        user_pass = request.POST.get('password')
        conf_pass = request.POST.get('password_confirmation')
        
        #DATA PROCESSING
        
        # NAME
        if len(user_name) > 2:
            
            name_split = user_name.split(' ')
            user_firstname = name_split[0]
            
            if len(name_split) > 1:
                user_lastname = user_name.replace(user_firstname,'').strip()
            else:
                user_lastname = ''
        
        else:
            
            alert.append('- Nome inválido.')
            
        # EMAIL
        user = User.objects.filter(username=user_mail).first()
        
        if valid_mail(user_mail):
            
            if user:
                
                alert.append('- E-mail já cadastrado.')
                
        else:
            
            alert.append('- E-mail inválido.')
            
        # CPF
        register = Userdata.objects.filter(register=user_register).first()
        
        if register:
            
            alert.append('- CPF já cadastrado.')
            
        else:
            
            if valid_cpf(user_register) == False:
                
                alert.append('- CPF inválido.')
            
        # PASSWORD
        if len(user_pass) < 8:
            
            alert.append('- A senha digitada é muito curta.')
            
        if user_pass != conf_pass:    
            
            alert.append('- As senhas não são iguais.')
            
        # INPUT ERROR
        if len(alert) != 0:
            
            context = {
                'type_alert':'alert-danger',
                'alert':alert,
                'user_name':user_name,
                'user_mail':user_mail,
                'user_cpf':user_register,
            }
            return render(request, 'signup.html', context)
        
        # INPUT REGISTER
        user_new = User.objects.create_user(username=user_mail, first_name=user_firstname, last_name=user_lastname, email=user_mail, password=user_pass)
        user_new.save()
        business = Business(owner_id=user_new.id,surname='Empresa Teste')
        business.save()
        user_data = Userdata(email=user_mail, register=user_register, level=1, business=business.id)
        user_data.save()
        
        context = {
            'type_alert':'alert-success',
            'alert':'Usuário cadastrado!',
            'user_mail':user_mail,
        }
        return render(request, 'signin.html', context)
    
    # LOGIN PAGE
    return render(request, 'signup.html')


### PAGE/SCRIPT - LOGIN
@csrf_protect
def signin(request):
    
    # LOGIN SCRIPT
    if request.method == 'POST':
        
        user_mail = request.POST.get('email')
        user_pass = request.POST.get('password')
        user_remember = request.POST.get('remember')
        
        user = authenticate(request, username=user_mail, password=user_pass)
        
        if user:
            
            login(request, user)
            if not user_remember:
                request.session.set_expiry(0) 
            return redirect('dashboard')
        
        else:
            
            context = {
                'type_alert':'alert-danger',
                'alert':'Usuário e senha inválido!',
                'user_mail':user_mail,   
            }
            return render(request, 'signin.html', context)
    
    # LOGIN PAGE
    return render(request, 'signin.html')


### PAGE/SCRIPT - RESET PASSWORD
@csrf_protect
def forgot(request):
    
    # FORGOT SCRIPT
    if request.method == 'POST':
        
        user_mail = request.POST.get('email')
        user = User.objects.filter(username=user_mail).first()
        
        # SCRIPT - MAIL DATA
        if user:
            
            subject, from_email, to = "Alteração de Senha", "IAS <muller@nocciolli.com.br>", user_mail
            html_content = f"<p>Esqueceu a senha do IAS?</p></br /><p>Clique no link abaixo, para visitar o endereço e alterar a sua senha.</p></br /><p><a href='https://ias.nocciolli.com.br/auth/reset/?mail={user_mail}'>https://ias.nocciolli.com.br/auth/reset/</a></p>"
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            
            # SCRIPT - SEND MAIL
            if msg:
                
                context = {
                    'type_alert':'alert-success',
                    'alert':'- E-mail enviado com sucesso!',
                }
                return render(request, 'forgot_success.html', context)
            
            else:
                
                context = {
                    'type_alert':'alert-danger',
                    'alert':'- O e-mail não pode ser enviado, tente novamente mais tarde.',
                }
                return render(request, 'forgot.html', context)
        
        # SCRIPT - INVALID MAIL
        context = {
            'type_alert':'alert-danger',
            'alert':'- E-mail inválido!',
        }
        return render(request, 'forgot.html', context)
    
    # FORGOT PAGE
    return render(request, 'forgot.html')


### PAGE/SCRIPT - RESET PASSWORD
@csrf_protect
def forgot_success(request):
    
    # FORGOT PAGE
    return render(request, 'forgot_success.html')


### PAGE/SCRIPT - RESET PASSWORD
@csrf_protect
def reset_password(request):
    
    # LOGIN SCRIPT
    if request.method == 'POST':
        pass
    
    # LOGIN PAGE
    pass


### SCRIPT
def signout(request):
    
    logout(request)
    
    return redirect('signin')