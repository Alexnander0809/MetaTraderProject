from django.db import models

class Cuenta(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    porcentaje_ganancia = models.DecimalField(max_digits=5, decimal_places=4)
    interes_compuesto = models.BooleanField(default=False)
    saldo_invertido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Historial(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    fecha = models.DateField()
    ingreso = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
