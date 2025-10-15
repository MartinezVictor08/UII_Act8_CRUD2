from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso

# Listar estudiantes
def index(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})

# Ver estudiante (opcional, puedes usarlo si quieres detalle)
def ver_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'listar_cursos.html', {'curso': curso})

# Agregar estudiante
def agregar_curso(request):
    if request.method == 'POST':
        nombre_curso = request.POST['nombre_curso']
        descripcion = request.POST['descripcion']
        duracion_semanas = request.POST['duracion_semanas']
        costo = request.POST['costo']
        numero_estudiantes = request.POST['numero_estudiantes']
       
        Curso.objects.create(nombre_curso=nombre_curso, descripcion=descripcion, duracion_semanas=duracion_semanas, costo=costo, numero_estudiantes=numero_estudiantes)
        return redirect('inicio')
    return render(request, 'agregar_curso.html')

# Editar estudiante
def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.nombre_curso = request.POST['nombre_curso']
        curso.descripcion = request.POST['descripcion']
        curso.duracion_semanas = request.POST['duracion_semanas']
        curso.costo = request.POST['costo']
        curso.numero_estudiantes = request.POST['numero_estudiantes']
        curso.save()
        return redirect('inicio')
    return render(request, 'editar_curso.html', {'curso': curso})

# Borrar estudiante
def borrar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('inicio')
    return render(request, 'borrar_curso.html', {'curso': curso})