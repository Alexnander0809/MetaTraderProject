from django.db import models
from clientes.models import Cliente

class Cuenta(models.Model):
    numero_cuenta = models.CharField(max_length=20)  # Aumentar longitud a 20 caracteres
    porcentaje_mensual = models.DecimalField(max_digits=5, decimal_places=2)  # Aumentar precisión
    porcentaje_diario = models.DecimalField(max_digits=5, decimal_places=4)  # Usar Decimal para mayor precisión
    total_invertido = models.DecimalField(max_digits=15, decimal_places=2)
    interes_compuesto = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)  # en meses

    def __str__(self):
        return f'Cuenta {self.id} - {self.cliente.nombre_completo}'

    class Meta:
        db_table = 'cuentas_cuenta'
