from django import forms
from .models import Vendas,Clientes


class VendaForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['produto', 'preco', 'quantidade', 'valor_total']
        widgets = {
            'produto': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome','cpf','nascimento','email','telefone','endereco','profissao']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'cpf': forms.NumberInput(attrs={'class':'form-control'}),
            'nascimento': forms.DateInput(attrs={'type':'date'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'telefone': forms.NumberInput(attrs={'class':'form-control'}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
            'profissao': forms.TextInput(attrs={'class':'form-control'}),
        }