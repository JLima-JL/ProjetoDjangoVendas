from django.urls import path
from vendas import views

urlpatterns = [
    path('vendas/', views.lista_vendas, name='listar_vendas'),
    path('cadastrar/', views.cadastrar_venda, name='cadastrar_venda'),
]
