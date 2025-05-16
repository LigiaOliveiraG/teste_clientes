from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    profissao = models.CharField(max_length=100, default='Não informado')

    def __str__(self):
        return self.nome
