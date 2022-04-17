from django.db import models

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)
    alcunha = models.CharField(max_length=100, null=True)


    def __str__(self) -> str:
        return self.nome_completo
    