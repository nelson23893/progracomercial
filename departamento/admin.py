#recuerde que es necesario indicar que clases de nuestro modelo van a ser manejadas por la aplicación /admin.
from django.contrib import admin
from departamento.models import Empleado, EmpleadoAdmin, Departamento, DepartamentoAdmin

#Registramos nuestras clases principales.
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)