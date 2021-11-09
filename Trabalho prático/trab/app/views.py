from django.forms.widgets import DateInput
from django.shortcuts import redirect, render
from app.forms import LivroForm
from app.models import Livro
# Create your views here.
def home(request):
    data = {}
    data['db'] = Livro.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = LivroForm
    return render(request, 'form.html', data)

def create(request):
    form = LivroForm(request.POST or None)
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