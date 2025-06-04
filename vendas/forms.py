from django import forms
from .models import Vendas, Clientes, Qualidade, Estoque


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

class VendaForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['cliente','produto', 'preco', 'quantidade', 'valor_total']
        widgets = {
            'produto': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
        }



class QualidadeForm(forms.ModelForm):
    class Meta:
        model = Qualidade
        fields = ['cliente','nota','num_compras','prod_comprado']
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-select'}),
            'nota': forms.NumberInput(attrs={'min':0,'max': 10}),
            'num_compras': forms.NumberInput(attrs={'class':'form-control'}),
            'prod_comprado': forms.TextInput(attrs={'class':'form-group'})
        }

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['nome_produto','quantidade','preco_uni']
        widgets = {
            'nome_produto': forms.TextInput(attrs={'class':'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class':'form-control'}),
            'preco_uni': forms.NumberInput(attrs={'class':'form-control'})

        }