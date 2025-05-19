from django.db import models

from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, null=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, null=True)
    acessorios = models.ManyToManyField(Acessorio, blank=True)

    def __str__(self):
        return f"({self.id}) {self.modelo}, {self.cor}, {self.ano} "
