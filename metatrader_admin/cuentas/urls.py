from django.urls import path
from .views import crear_cuenta, lista_cuenta, actualizar_cuenta

urlpatterns = [
    path('crear_cuenta/', crear_cuenta, name='crear_cuenta'),  # Vista principal de cuentas
    path('lista_cuenta/', lista_cuenta, name='lista_cuenta'),  # Ejemplo de una vista de perfil
    path('actualizar_cuenta/<int:cuenta_id>', actualizar_cuenta, name='actualizar_cuenta'),
]
