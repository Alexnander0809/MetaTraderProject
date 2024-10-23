from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Cuenta
from clientes.models import Cliente
from decimal import Decimal, InvalidOperation

def crear_cuenta(request):
    if request.method == 'POST':
        numero_cuenta = request.POST.get('numero_cuenta', '').strip()
        porcentaje_mensual = request.POST.get('porcentaje_mensual', '').strip()
        porcentaje_diario = request.POST.get('porcentaje_diario', '').strip()
        total_invertido = request.POST.get('total_invertido', '').strip()
        interes_compuesto = request.POST.get('interes_compuesto', '') == 'True'
        estado = 'Activo'
        cliente_id = request.POST.get('cliente', '')

        if Cuenta.objects.filter(numero_cuenta=numero_cuenta).exists():
            messages.error(request, "El número de cuenta ya existe. Por favor, ingrese un número diferente.")
            return redirect('crear_cuenta')

        cliente = get_object_or_404(Cliente, id=cliente_id)
        if Cuenta.objects.filter(cliente=cliente).exists():
            messages.error(request, "El cliente seleccionado ya tiene una cuenta asignada.")
            return redirect('crear_cuenta')

        try:
            total_invertido_clean = total_invertido.replace('$', '').replace('.', '').replace(',', '.')
            total_invertido_decimal = Decimal(total_invertido_clean)
        except (InvalidOperation, ValueError):
            messages.error(request, "El valor ingresado para 'Total invertido' no es válido.")
            return redirect('crear_cuenta')

        try:
            porcentaje_mensual_decimal = Decimal(porcentaje_mensual)
        except (InvalidOperation, ValueError):
            messages.error(request, "El valor ingresado para 'Porcentaje mensual' no es válido.")
            return redirect('crear_cuenta')

        try:
            porcentaje_diario_decimal = Decimal(porcentaje_diario)
        except (InvalidOperation, ValueError):
            messages.error(request, "El valor ingresado para 'Porcentaje diario' no es válido.")
            return redirect('crear_cuenta')

        Cuenta.objects.create(
            numero_cuenta=numero_cuenta,
            porcentaje_mensual=porcentaje_mensual_decimal,
            porcentaje_diario=porcentaje_diario_decimal,
            total_invertido=total_invertido_decimal,
            interes_compuesto=interes_compuesto,
            cliente=cliente,
            estado=estado
        )
        messages.success(request, "Cuenta creada exitosamente.")
        return redirect('lista_cuenta')

    clientes = Cliente.objects.all()
    return render(request, 'cuentas/crear_cuenta.html', {'clientes': clientes})

def lista_cuenta(request):
    filter_type = request.GET.get('filter')
    search_cedula = request.GET.get('cedula')

    if filter_type == 'active':
        cuentas = Cuenta.objects.filter(estado='Activo')
    elif filter_type == 'inactive':
        cuentas = Cuenta.objects.filter(estado='Inactivo')
    elif filter_type == 'all':
        cuentas = Cuenta.objects.all()
    else:
        cuentas = Cuenta.objects.all()

    if search_cedula:
        cuentas = cuentas.filter(cedula__icontains=search_cedula)

    return render(request, 'cuentas/lista_cuenta.html', {'cuentas': cuentas})

def actualizar_cuenta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        porcentaje_mensual = request.POST.get('porcentaje_mensual', '').strip()
        total_invertido = request.POST.get('total_invertido', '').strip()
        interes_compuesto = request.POST.get('interes_compuesto', '') == 'True'
        estado = request.POST.get('estado', '')
        cliente_id = request.POST.get('cliente', '').strip()

        # Validar longitud de numero_cuenta
        if len(request.POST.get('numero_cuenta', '').strip()) > 13:
            messages.error(request, "El número de cuenta no puede tener más de 13 caracteres.")
            return render(request, 'cuentas/actualizar_cuenta.html', {'cuenta': cuenta, 'clientes': clientes})

        # Limpiar y convertir 'total_invertido' a decimal
        try:
            total_invertido_clean = total_invertido.replace('$', '').replace('.', '').replace(',', '.')
            cuenta.total_invertido = Decimal(total_invertido_clean)
        except (InvalidOperation, ValueError):
            messages.error(request, "El valor ingresado para 'Total invertido' no es válido.")
            return render(request, 'cuentas/actualizar_cuenta.html', {'cuenta': cuenta, 'clientes': clientes})

        # Validar y convertir cliente_id
        try:
            cliente_id_int = int(cliente_id)
            cliente = Cliente.objects.get(id=cliente_id_int)  # Verifica si el cliente existe
        except (ValueError, Cliente.DoesNotExist):
            messages.error(request, "ID de cliente inválido o el cliente no existe.")
            return render(request, 'cuentas/actualizar_cuenta.html', {'cuenta': cuenta, 'clientes': clientes})

        # Validar y convertir porcentaje_mensual
        try:
            porcentaje_mensual_decimal = Decimal(porcentaje_mensual) / 100  # Convertir a decimal (e.g., 5% -> 0.05)
            cuenta.porcentaje_mensual = porcentaje_mensual_decimal

            # Calcular porcentaje diario basado en porcentaje mensual
            if porcentaje_mensual_decimal > 0:
                porcentaje_diario_decimal = (Decimal(1) + porcentaje_mensual_decimal)**(Decimal(1)/30) - Decimal(1)
                cuenta.porcentaje_diario = porcentaje_diario_decimal * 100  # Convertir a porcentaje (e.g., 0.05 -> 5%)
            else:
                cuenta.porcentaje_diario = Decimal(0)
        except (InvalidOperation, ValueError):
            messages.error(request, "El valor ingresado para 'Porcentaje mensual' no es válido.")
            return render(request, 'cuentas/actualizar_cuenta.html', {'cuenta': cuenta, 'clientes': clientes})

        cuenta.interes_compuesto = interes_compuesto
        cuenta.estado = estado
        cuenta.cliente = cliente
        cuenta.save()

        messages.success(request, "Cuenta actualizada exitosamente.")
        return redirect('lista_cuenta')

    return render(request, 'cuentas/actualizar_cuenta.html', {'cuenta': cuenta, 'clientes': clientes})