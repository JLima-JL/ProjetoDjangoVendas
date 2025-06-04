from django.urls import path
from . import views

urlpatterns = [
    path('vendas/', views.lista_vendas, name='listar_vendas'),
    path('cadastrar/', views.cadastrar_venda, name='cadastrar_venda'),
    path('cliente/cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente/',views.listar_clientes, name='listar_clientes'),
    path('qualidade/',views.qualidade,name='cadastro_qualidade'),
    path('qualidade/listar_qualidade',views.listar_qualidade,name='listar_qualidade'),
    path('avaliacoes/editar/<int:pk>/', views.editar_qualidade, name='editar_qualidade'),
    path('avaliacoes/excluir/<int:pk>/', views.excluir_qualidade, name='excluir_qualidade'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('estoque/', views.estoque,name='estoque_cadastro'),
    path('estoque/listar_estoque',views.listar_estoque,name='listar_estoque')


]
