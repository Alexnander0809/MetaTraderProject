from django.urls import path
from .views import crear_inversion, lista_inversion

urlpatterns = [
    path('crear_inversion/', crear_inversion, name='crear_inversion'),  # Vista principal de inversiones
    path('lista_inversion/', lista_inversion, name='lista_inversion'),  # Ejemplo de detalle de inversión
] 
