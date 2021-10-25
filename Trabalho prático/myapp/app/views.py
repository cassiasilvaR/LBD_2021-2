from django.shortcuts import render
from django.http import HttpResponse #site do danjo?
# Create your views here.
def index(request): #O que for colocado aqui vai ser mostrado pro usuário
    return HttpResponse('<h1> Olá </h1>') #Header