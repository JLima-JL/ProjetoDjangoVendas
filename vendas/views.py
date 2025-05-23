from .models import Vendas
from django.shortcuts import render, redirect
from .forms import VendaForm

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

