from django.shortcuts import render


# Página inicial do site
def index(request):
    
    if request.method == 'POST':
        pass
    
    return render(request, 'index.html')


# Script de envio de mensagens
def contact(request):
    pass