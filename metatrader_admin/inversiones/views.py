from django.shortcuts import render

def crear_inversion(request):
    return render(request, 'inversiones/crear_inversion.html')

def lista_inversion(request):
    return render(request, 'inversiones/lista_inversion.html')
