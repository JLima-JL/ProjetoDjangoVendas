from .models import Vendas, Clientes
from django.shortcuts import render, redirect
from .forms import VendaForm, ClienteForm

def cadastrar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vendas')
    else:
        form = VendaForm()
    return render(request, 'vendas/form_venda.html', {'form': form})



def lista_vendas(request):
    vendas = Vendas.objects.all()
    return render(request, 'vendas/lista.html', {'vendas': vendas})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes.html')
    else:
        form = ClienteForm()
    return render(request,'vendas/cadastro_cliente.html', {'form': form})

def listar_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'vendas/lista_clientes.html', {'clientes': clientes})