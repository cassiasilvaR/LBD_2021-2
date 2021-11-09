from typing import NoReturn
from django.forms.widgets import DateInput, DateTimeBaseInput
from django.shortcuts import redirect, render
from app.forms import EmprestimoForm, EscritorForm, EstanteForm, LivroForm, UsuarioForm
from app.models import Escritor, Livro
# Create your views here.
def home(request):
    data = {}
    data['db'] = Livro.objects.all()
    data['dbe'] = Escritor.objects.all()
    return render(request, 'index.html', data)

def form_e(request):
    data = {}
    data['form'] = EscritorForm
    return render(request, 'form_e.html', data)  

def emprestar(request, pk):
    data = {}
    data['db'] = Livro.objects.get(pk=pk)
    return render(request, 'emprestar.html', data)

def form(request):
    data = {}
    data['form'] = LivroForm
    return render(request, 'form.html', data)

def form_user(request):
    data = {}
    data['form'] = UsuarioForm
    return render(request, 'form_user.html', data)

def create_user(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def create(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return  redirect('home')

def create_e(request):
    form = EscritorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return  redirect('home')    

def view(request, pk):
    data = {}
    data['db'] = Livro.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Livro.objects.get(pk=pk)
    data['form'] = LivroForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Livro.objects.get(pk=pk)
    form = LivroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def update_e(request, pk):
    data = {}
    data['db'] = Escritor.objects.get(pk=pk)
    form = EscritorForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')