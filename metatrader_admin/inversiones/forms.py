from django import forms
from .models import HistorialInversion

class HistorialInversionForm(forms.ModelForm):
    class Meta:
        model = HistorialInversion
        fields = ['cuenta', 'monto']
