from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inversion, Cuenta
from django.views.decorators.http import require_POST

def crear_inversion(request):
    if request.method == 'POST':
        cuenta_id = request.POST.get('cuenta_id')
        monto = request.POST.get('monto')

        if not cuenta_id or not monto:
            return HttpResponse("Todos los campos son obligatorios.", status=400)

        try:
            cuenta = Cuenta.objects.get(id=cuenta_id)
        except Cuenta.DoesNotExist:
            return HttpResponse("La cuenta especificada no existe.", status=400)

        try:
            monto = float(monto.replace('.', '').replace(',', '.').replace('$', ''))  # Convertir el monto a número
            if monto <= 0:
                return HttpResponse("El monto debe ser un número positivo.", status=400)
        except ValueError:
            return HttpResponse("El monto debe ser un número válido.", status=400)

        # Crear la inversión
        inversion = Inversion(cuenta=cuenta, monto=monto)
        inversion.save()

        # Actualizar el total_invertido de la cuenta
        cuenta.total_invertido += monto
        cuenta.save()

        return redirect('lista_inversion')  # Redirigir a la lista de inversiones después de guardar

    cuentas = Cuenta.objects.all()
    return render(request, 'inversiones/crear_inversion.html', {'cuentas': cuentas})


def lista_inversion(request):
    inversiones = Inversion.objects.all()
    return render(request, 'inversiones/lista_inversion.html', {'inversiones': inversiones})
