from django.urls import path, include

urlpatterns = [
    path('cuentas/', include('cuentas.urls')),
    path('inversiones/', include('inversiones.urls')),
    # otras rutas
]
