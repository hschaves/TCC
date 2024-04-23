from django import forms
from .models import Notebook

class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ['modelo', 'processador', 'memoria_gb', 'armazenamento_gb', 'data_compra', 'usuario', 'status']
