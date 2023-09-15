from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    observacoes = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10, unique=True)
    agencia = models.CharField(max_length=10)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Conta {self.numero} - Agência {self.agencia}"
