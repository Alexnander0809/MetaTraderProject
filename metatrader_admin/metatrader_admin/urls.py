from django.contrib import admin
from django.urls import path, include
from .views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='principal'),  # Redirige la vista principal a 'cuentas' o donde quieras
    path('clientes/', include('clientes.urls')),
    path('cuentas/', include('cuentas.urls')),
    path('inversiones/', include('inversiones.urls')),
]
