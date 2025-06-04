from .models import Vendas, Clientes, Qualidade, Estoque
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VendaForm, ClienteForm, QualidadeForm, EstoqueForm
from datetime import timedelta, date

def cadastrar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vendas')
    else:
        form = VendaForm()
    return render(request, 'vendas/form_venda.html', {'form': form})



def lista_vendas(request):
    vendas = Vendas.objects.all()
    return render(request, 'vendas/lista.html', {'vendas': vendas})


def estoque(request):
    if request.method == 'POST':
        form = EstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estoque')
    else:
        form = EstoqueForm()
    return render(request,'vendas/estoque_cadastro.html',{'form': form})


def listar_estoque(request):
    estoque = Estoque.objects.all()
    return render(request,'vendas/listar_estoque.html',{'estoque': estoque})

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


def qualidade(request):
    if request.method == 'POST':
        form = QualidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_qualidade.html')
    else:
        form = QualidadeForm()
    return render(request,'vendas/qualidade.html', {'form': form})


def listar_qualidade(request):
    qualidade = Qualidade.objects.all()
    return render(request, 'vendas/listar_qualidade.html', {'qualidade': qualidade})

def editar_qualidade(request, pk):
    qualidade = get_object_or_404(Qualidade, pk=pk)
    if request.method == 'POST':
        form = QualidadeForm(request.POST, instance=qualidade)
        if form.is_valid():
            form.save()
            return redirect('listar_qualidade')
    else:
        form = QualidadeForm(instance=qualidade)
    return render(request, 'vendas/qualidade.html', {'form': form})

def excluir_qualidade(request, pk):
    qualidade = get_object_or_404(Qualidade, pk=pk)
    qualidade.delete()
    return redirect('listar_qualidade')

def dashboard(request):
    hoje : date.today()

    return render(request,'vendas/dashboard.html')
