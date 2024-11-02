#Aqui é aonde são renderizadoas as coisas, páginas e etc.
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import FormLinks

# Create your views here.
def home(request):
    form = FormLinks()
    return render(request, 'home.html', {'form': form})