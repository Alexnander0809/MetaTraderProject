from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Cuenta
from clientes.models import Cliente

def crear_cuenta(request):
    if request.method == 'POST':
        porcentaje_diario = request.POST['porcentaje_diario']
        monto_invertido = request.POST['monto_invertido']
        interes_compuesto = request.POST['interes_compuesto'] == 'True'
        clausula_tiempo = request.POST['clausula_tiempo']
        cliente_id = request.POST['cliente']
        estado = request.POST['estado']

        cliente = get_object_or_404(Cliente, id=cliente_id)

        Cuenta.objects.create(
            porcentaje_diario=porcentaje_diario,
            monto_invertido=monto_invertido,
            interes_compuesto=interes_compuesto,
            clausula_tiempo=clausula_tiempo,
            cliente=cliente,
            estado=estado
        )
        messages.success(request, "Cuenta creada exitosamente.")
        return redirect('lista_cuenta')

    clientes = Cliente.objects.all()
    return render(request, 'cuentas/crear_cuenta.html', {'clientes': clientes})

def lista_cuenta(request):
    cuentas = Cuenta.objects.all()
    return render(request, 'cuentas/lista_cuenta.html', {'cuentas': cuentas})

def actualizar_cuenta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        cuenta.porcentaje_diario = request.POST['porcentaje_diario']
        cuenta.monto_invertido = request.POST['monto_invertido']
        cuenta.interes_compuesto = request.POST['interes_compuesto'] == 'True'
        cuenta.clausula_tiempo = request.POST['clausula_tiempo']
        cuenta.cliente = get_object_or_404(Cliente, id=request.POST['cliente'])
        cuenta.estado = request.POST['estado']
        cuenta.save()
        messages.success(request, "Cuenta actualizada exitosamente.")
        return redirect('lista_cuenta')

    return render(request, 'cuentas/actualizar_cuenta.html', {'cuenta': cuenta, 'clientes': clientes})
