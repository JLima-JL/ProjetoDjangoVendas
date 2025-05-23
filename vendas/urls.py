from django.urls import path
from . import views

urlpatterns = [
    path('vendas/', views.lista_vendas, name='listar_vendas'),
    path('cadastrar/', views.cadastrar_venda, name='cadastrar_venda'),
    path('cliente/cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente/',views.listar_clientes, name='listar_clientes')
]
