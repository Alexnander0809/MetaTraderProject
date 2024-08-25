from django import forms
from .models import Cuenta

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['cliente', 'porcentaje_diario', 'monto_invertido', 'interes_compuesto', 'clausula_tiempo']
