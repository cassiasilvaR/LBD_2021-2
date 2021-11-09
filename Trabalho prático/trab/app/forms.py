from django.forms import ModelForm
from app.models import Livro

# Create the form class.
class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'edicao', 'ano', 'ibsn']
