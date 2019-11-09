from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import EmpleadoForm, PForm     
from .models import Empleado, Departamento, Mains
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def empleado_list(request):
    posts = Empleado.objects.all()
    return render(request, 'empleados/empleado_list.html', {'posts': posts})
@login_required
def empleado_details(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    mains = Mains.objects.filter(jugador=pk)
    return render(request, 'empleados/empleados_details.html', {'empledos': empleado, 'mains': mains })

@login_required
def departamento_list(request):
    posts = Departametno.objects.all()
    return render(request, 'departamento/departamento_list.html', {'posts': posts})

@login_required
def empleado_nuevo(request):
    if request.method == "POST":
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            empleado = Empleado.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for personaje_id in request.POST.getlist('personajes'):
                mains = Mains(departamento_id=departamento_id, empleado_id = empleado.id)
                mains.save()
            messages.add_message(request, messages.SUCCESS, 'Empleado Guardado Exitosamente')
            return redirect('empleado_list')
    else:
        formulario = EmpleadosForm()
    return render(request, 'empleados/editar.html', {'formulario': formulario})

@login_required
def empleado_edit(request, pk):
    post = get_object_or_404(EMpleado, pk=pk)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            for departametnto_id in request.POST.getlist('departamento'):
                mains = Mains(departamento_id=departamento_id, empleado_id = pk)
            for departamentos_id in request.POST.getlist('departamentos'):
                mains = Mains(departamento_id=departamento_id, jugador_id = pk)
                mains.save()
            post.save()
            return redirect('empleado_list')
    else:
        form = JugadorForm(instance=post)
    return render(request, 'empleados/agregar.html', {'form': form})

def departamento_nueva(request):
    if request.method == "POST":
        formulario = DepartamentoForm(request.POST)
        if formulario.is_valid():
            departamento = Departamento.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for empleado_id in request.POST.getlist('empleados'):
                puesto = Puesto(empleado_id=empleado_id, departamento_id = departamento.id)
                puesto.save()
            messages.add_message(request, messages.SUCCESS, 'Departamento Guardada Exitosamente')
    else:
        formulario = DepartamentoForm()
    return render(request, 'departamento/departamento_editar.html', {'formulario': formulario})

@login_required
def empleado_delete(request, pk):
    post = get_object_or_404(Empleado, pk=pk)
    post.delete()
    return redirect('empleado_list')

@login_required
def departamento_edit(request, pk):
    post = get_object_or_404(Departamento, pk=pk)
    if request.method == "POST":
        form = PForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('departamento_list')
    else:
        form = DepartamentoForm(instance=post)
    return render(request, 'empleados/agregar.html', {'form': form})

@login_required
def departamento_details(request, pk):
    post = get_object_or_404(DepartamentoForm, pk=pk)
    mains = Mains.objects.filter(departamento=pk)
    return render(request, 'empleados/departamento_details.html', {'post': post,'mains': mains})

@login_required
def departamento_delete(request, pk):
    post = get_object_or_404(Departamento, pk=pk)
    post.delete()
    return redirect('departamento_list')