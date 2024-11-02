#Aqui é aonde são renderizadoas as coisas, páginas e etc.
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormLinks
from .models import Links

# Create your views here.
def home(request):
    form = FormLinks()
    status = request.GET.get('status')

    return render(request, 'home.html', {'form': form, 'status': status})

def valida_link(request):
    form = FormLinks(request.POST)

    #Verifica se  o nome do link encurtado é unico, se não for, redireciona para a home
    link_encurtado = form.data['link_encurtado']
    links = Links.objects.filter(link_encurtado = link_encurtado)
    if len(links) > 0:
        return redirect("/?status=1")

    if form.is_valid():
        try:
            form.save()
            return HttpResponse(f'Seu link foi criado, ele é: https://www.encurt.com/{link_encurtado}')
        except:
            return HttpResponse("Erro interno ao salvar")