# IMPORT REQUIREMENTS
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from authentication.validators import valid_cpf, valid_mail
from django.utils.crypto import get_random_string
# IMPORT MODELS
from django.contrib.auth.models import User
from authentication.models import Userdata
from system.business.models import Business



def maintenance(request):
    return render(request, 'maintenance.html')



@csrf_protect
def signup(request):
    

    if request.method == 'POST':
        

        alert = []
        
        user_name = request.POST.get('name')
        user_register = request.POST.get('register')
        user_mail = request.POST.get('email')
        user_pass = request.POST.get('password')
        conf_pass = request.POST.get('password_confirmation')
        

        if len(user_name) > 2:
            
            name_split = user_name.split(' ')
            user_firstname = name_split[0]
            
            if len(name_split) > 1:
                user_lastname = user_name.replace(user_firstname,'').strip()
            else:
                user_lastname = ''
        
        else:
            
            alert.append('- Nome inválido.')
            

        user = User.objects.filter(username=user_mail).first()
        
        if valid_mail(user_mail):
            
            if user:
                
                alert.append('- E-mail já cadastrado.')
                
        else:
            
            alert.append('- E-mail inválido.')
            

        register = Userdata.objects.filter(register=user_register).first()
        
        if register:
            
            alert.append('- CPF já cadastrado.')
            
        else:
            
            if valid_cpf(user_register) == False:
                
                alert.append('- CPF inválido.')
            

        if len(user_pass) < 8:
            
            alert.append('- A senha digitada é muito curta.')
            
        if user_pass != conf_pass:    
            
            alert.append('- As senhas não são iguais.')
            

        if len(alert) != 0:
            
            context = {
                'type_alert':'alert-danger',
                'alert':alert,
                'user_name':user_name,
                'user_mail':user_mail,
                'user_cpf':user_register,
            }
            return render(request, 'signup.html', context)


        user_new = User.objects.create_user(username=user_mail, first_name=user_firstname, last_name=user_lastname, password=user_pass)
        user_new.save()

        business = Business(token=get_random_string(length=16),surname='Empresa Teste')
        business.save()

        user_data = Userdata(email=user_mail, register=user_register, level=1, business=business.token)
        user_data.save()
        
        context = {
            'type_alert':'alert-success',
            'alert':'Usuário cadastrado!',
            'user_mail':user_mail,
        }
        return render(request, 'signin.html', context)
    

    return render(request, 'signup.html')



@csrf_protect
def signin(request):
    

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
    

    return render(request, 'signin.html')



@csrf_protect
def forgot(request):
    

    if request.method == 'POST':
        
        user_mail = request.POST.get('email')
        user = User.objects.filter(username=user_mail).first()
        

        if user:
            
            subject, from_email, to = "Alteração de Senha", "IAS <muller@nocciolli.com.br>", user_mail
            html_content = f"<p>Esqueceu a senha do IAS?</p></br /><p>Clique no link abaixo, para visitar o endereço e alterar a sua senha.</p></br /><p><a href='https://ias.nocciolli.com.br/auth/reset/?mail={user_mail}'>https://ias.nocciolli.com.br/auth/reset/</a></p>"
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            

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
            
        
        context = {
            'type_alert':'alert-danger',
            'alert':'- E-mail inválido!',
        }
        return render(request, 'forgot.html', context)
    

    return render(request, 'forgot.html')



@csrf_protect
def forgot_success(request):


    return render(request, 'forgot_success.html')



@csrf_protect
def reset_password(request):
    

    if request.method == 'POST':
        pass
    

    pass



def signout(request):
    

    logout(request)
    

    return redirect('signin')