from django.shortcuts import render, redirect
from .models import Cuenta
from .forms import CuentaForm
from datetime import datetime, timedelta

def crear_cuenta(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cuentas')
    else:
        form = CuentaForm()
    return render(request, 'cuentas/crear_cuenta.html', {'form': form})


def actualizar_ganancias():
    hoy = datetime.today().date()
    cuentas = Cuenta.objects.all()
    for cuenta in cuentas:
        # Lógica para calcular y actualizar ganancias
        pass
