from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from app.models import Emprestimo, Escritor, Estante, Livro, Usuario

# Create the form class.
class EscritorForm(ModelForm):
    class Meta:
        model = Escritor
        fields = ['nome', 'area_atuacao']
        
class EstanteForm(ModelForm):
    class Meta:
        model = Estante
        fields = ['categoria']

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'edicao', 'ano', 'ibsn', 'escritor', 'estante']

class UsuarioForm(ModelForm):
    class Meta: 
        model = Usuario
        fields = ['nome']

class EmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'usuario']
