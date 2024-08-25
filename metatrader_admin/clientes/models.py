from django.db import models

class Cliente(models.Model):
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cliente'  # Este es el nombre de la tabla que quieres
