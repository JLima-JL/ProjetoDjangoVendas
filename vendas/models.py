from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Clientes(models.Model):
    nome = models.TextField(blank=False)
    cpf = models.CharField(max_length=14,blank=False,unique=True)
    nascimento = models.DateField(blank=False)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=15,blank=False)
    endereco = models.TextField(blank=False)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    profissao = models.TextField()
    renda = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    data_cadastro = models.DateField(auto_now_add=True)

    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.nascimento.year - (
                (hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day)
        )

    def __str__(self):
        return f"{self.nome} - {self.telefone}" \
               f"{self.endereco}" \
               f"{self.email}"
class Estoque(models.Model):
    nome_produto = models.TextField(blank=False)
    quantidade = models.IntegerField(blank=False)
    preco_uni = models.DecimalField(max_digits=10,decimal_places=2)

class Vendas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE,null=True)
    data = models.DateField(auto_now_add=True)
    produto = models.ForeignKey(Estoque,on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self,*args,**kwargs):
        self.valor_total = self.preco * self.quantidade

        if self._state.adding:
            if self.quantidade > self.produto.quantidade:
                raise ValueError("Quantidade excede estoque disponivel")

            self.produto.quantidade -= self.quantidade
            self.produto.save_form_data()

        super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.produto} - {self.quantidade}" \
               f"{self.data} - {self.valor_total}"




class Qualidade(models.Model):
    cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE, null=True)
    data = models.DateField(auto_now_add=True)
    nota = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)], null=True)
    num_compras = models.IntegerField()
    prod_comprado = models.TextField()

    def __str__(self):
        return f"{self.cliente.nome} - {self.num_compras}"\
               f"{self.cliente.email} - {self.cliente.telefone}"


