from django import forms
from .models import Departamento, Empleado

class DepartamentoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Departamento
        fields = ('nombre', 'anio', 'empleados')

    def __init__ (self, *args, **kwargs):
        super(DepartamentoForm, self).__init__(*args, **kwargs)
        self.fields["empleados"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["empleados"].help_text = "Ingrese los Empleado en la Departamento"
        self.fields["empleados"].queryset = Empleado.objects.all()
