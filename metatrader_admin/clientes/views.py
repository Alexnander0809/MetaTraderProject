from django.shortcuts import get_object_or_404, render, redirect
from .models import Cliente
from django.contrib import messages
# from .forms import ClienteFilterForm

def crear_cliente(request):
    if request.method == 'POST':
        cedula = request.POST['cedula']
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']

        # Validar y guardar datos
        if cedula and nombre and email and telefono and direccion:
            cliente = Cliente(cedula = cedula, nombre=nombre, email=email, telefono=telefono, direccion=direccion)
            cliente.save()
            messages.success(request, 'Cliente añadido exitosamente.')
            return redirect('lista_cliente')  # Cambia esta línea a la URL correspondiente
        else:
            messages.error(request, 'Todos los campos son requeridos.')

    return render(request, 'clientes/crear_cliente.html')

def lista_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_cliente.html', {'clientes': clientes})

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)  # Obtén el cliente con el ID proporcionado
    
    if request.method == 'POST':
        # Obtener los datos del formulario
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        estado = request.POST.get('estado')  # Obtener el estado del formulario

        # Actualizar los datos del cliente
        cliente.cedula = cedula
        cliente.nombre = nombre
        cliente.email = email
        cliente.telefono = telefono
        cliente.direccion = direccion
        cliente.estado = estado  # Actualizar el estado del cliente
        cliente.save()  # Guarda los cambios en la base de datos

        messages.success(request, 'Cliente actualizado exitosamente.')
        return redirect('lista_cliente')  # Redirige a una vista después de actualizar, por ejemplo, la lista de clientes
    else:
        # Si no es un POST, mostramos el formulario con los datos actuales del cliente
        context = {
            'cliente': cliente
        }
        return render(request, 'clientes/actualizar_cliente.html', context)