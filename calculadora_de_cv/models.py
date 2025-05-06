from django.db import models

from calculadora_de_cv.calcs import calcular_valor_critico


class Artefato(models.Model):
    dano_critico = models.FloatField()
    taxa_critica = models.FloatField()
    valor_critico = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.valor_critico is None:
            self.valor_critico = calcular_valor_critico(dano_critico=float(self.dano_critico), taxa_critica=float(self.taxa_critica))
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.valor_critico)
