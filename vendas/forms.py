from django import forms
from .models import Vendas


class VendaForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['produto', 'preco', 'quantidade', 'valor_total']  # ← data removido
        widgets = {
            'produto': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
        }

