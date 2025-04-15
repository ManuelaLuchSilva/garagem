from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80)
    categoria = models.CharField(max_length=80) 
    def __str__(self):
        return f"({self.id}) {self.marca}, {self.nome.upper()} "