from typing import NoReturn
from django.db.models import query
from django.db.models.expressions import When
from django.db.models.sql.query import RawQuery
from django.forms.widgets import DateInput, DateTimeBaseInput, Select
from django.shortcuts import redirect, render
from app.forms import EmprestimoForm, EscritorForm, EstanteForm, LivroForm, UsuarioForm
from app.models import Emprestimo, Escritor, Livro, Usuario, Estante
# Create your views here.
def home(request):
    data = {}
    data['db'] = Livro.objects.raw("Select * from app_livro where id not in (select livro_id from app_emprestimo)")
    data['dbe'] = Escritor.objects.all()
    return render(request, 'index.html', data)

def form_e(request):
    data = {}
    data['form'] = EscritorForm
    return render(request, 'form_e.html', data)  

def form_est(request):
    data = {}
    data['form'] = EstanteForm
    return render(request, 'form_est.html', data) 

def registestante(request):
    form = EstanteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return  redirect('home')  

def emprestar(request, pk):
    data = {}
    data['db'] = Livro.objects.get(pk=pk)
    data['user'] = Usuario.objects.all()#objects.all()
    data['form'] = EmprestimoForm
    return render(request, 'emprestar.html', data)

def emprestimo(request):
    form = EmprestimoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def form(request):
    data = {}
    data['form'] = LivroForm
    data['escritor'] = Escritor.objects.all()
    data['estante'] = Estante.objects.all()
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
    
def delete(request, pk):
    db = Livro.objects.get(pk=pk)
    db.delete()
    return redirect('home')