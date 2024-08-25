from django.db import models
from cuentas.models import Cuenta

# Create your models here.
class HistorialInversion(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return f'Historial {self.id} - {self.cuenta.id}'