from django.db import models


class Vendas(models.Model):
    data = models.DateField(auto_now_add=True)
    produto = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self,*args,**kwargs):
        self.valor_total = self.preco * self.quantidade
        super().save(*args,**args)

    def __str__(self):
        return f"{self.produto} - {self.quantidade}" \
               f"{self.data} - {self.valor_total}"

class Clientes(models.Model):
    nome = models.TextField(blank=False)
    cpf = models.CharField(max_length=14,blank=False,unique=True)
    nascimento = models.DateField(blank=False)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=15,blank=False)
    endereco = models.TextField(blank=False)
    profissao = models.TextField()
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.telefone}" \
               f"{self.endereco}" \
               f"{self.email}"