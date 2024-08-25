from django.urls import path
from .views import crear_cliente, lista_cliente, actualizar_cliente

urlpatterns = [
    path('crear_cliente/', crear_cliente, name='crear_cliente'),  # Vista principal de cuentas
    path('lista_cliente/', lista_cliente, name='lista_cliente'),  # Ejemplo de una vista de perfil
    path('actualizar_cliente/<int:id>', actualizar_cliente, name='actualizar_cliente'),
]
