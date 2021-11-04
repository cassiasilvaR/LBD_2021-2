from types import resolve_bases
from django.shortcuts import render
from django.http import HttpResponse #site do danjo?
# Create your views here.
def index(request): #O que for colocado aqui vai ser mostrado pro usuário
    info = {
        'nome' : 'Cassia',
        'idade': 19,
        'naturalidade' : 'Pará'
    }
    return render(request, 'index.html', info) #HttpResponse('<h1> Olá </h1>') #Header

def counter(request):
    words = request.GET['words']
    amount_words = len(words.split())
    return render(request, 'counter.html', {'amount' : amount_words})