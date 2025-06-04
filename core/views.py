from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from .models import *
from django.core.serializers import serialize
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
from .forms import TotemValidationForm


# Create your views here.

def login(request):
    return render(request,'core/login.html')

def diseno(request):
    disenoImg = Totem.objects.all()
    beneficios = Beneficio.objects.all()
    cursolistado = Curso.objects.all()
    alumnolist = Alumno.objects.all()
    return render(request,'core/diseno.html' ,{"img":disenoImg, "beneficios": beneficios, "cursos": cursolistado, "alumnos": alumnolist})




# home fablab
def index(request):                    
    return render(request,"core/index.html") 







#Vistas Docente
def agregarDocentes(request):
    if request.method == 'POST':           
        if request.POST.get('nombre') and request.POST.get('rut') and request.POST.get('email') and request.POST.get('areaAcademica'):
            docentes = Docente()
            docentes.nombre = request.POST.get('nombre')
            docentes.rut = request.POST.get('rut')
            docentes.email = request.POST.get('email')
            docentes.areaAcademica = request.POST.get('areaAcademica')
            docentes.save()
            return redirect('listarDocentes')
    else:
        return render(request,"core/crud_docentes/agregar_d.html") 

def listarDocentes(request):

    return render(request,"core/crud_docentes/listar_d.html",{ 'docentes' : Docente.objects.all()}) 



def actualizarDocentes(request):
    if request.method == 'POST':
        rut_a_actualizar = request.POST.get('RUT')

        # Asegurarse de que el RUT no esté vacío
        if not rut_a_actualizar:

            return JsonResponse({'error': 'El RUT no puede estar vacío'})

        try:
            docente_a_actualizar = Docente.objects.get(rut=rut_a_actualizar)
        except Docente.DoesNotExist:
            # Manejar el caso en el que el docente no existe
            return JsonResponse({'error': 'El docente no existe'})

        # Resto de tu código para actualizar el docente
        docente_a_actualizar.nombre = request.POST.get('nombre')
        docente_a_actualizar.email = request.POST.get('email')
        docente_a_actualizar.areaAcademica = request.POST.get('areaAcademica')
        docente_a_actualizar.save()

        return redirect('listarDocentes')  # Redirige a la página de listado después de la actualización

    else:
        docentes = Docente.objects.all()
        return render(request, "core/crud_docentes/actualizar_d.html", {'docentes': docentes})


def eliminarDocentes(request):
    if request.method == 'POST':
        rut_a_eliminar = request.POST.get('RUT')
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        area_academica = request.POST.get('areaAcademica')

        # Recupera la instancia del Docente que  actualiza
        docente_a_eliminar = Docente.objects.get(rut=rut_a_eliminar)

        # Actualiza los campos del Docente
        docente_a_eliminar.nombre = nombre
        docente_a_eliminar.email = email
        docente_a_eliminar.areaAcademica = area_academica

        # Guarda los cambios
        docente_a_eliminar.delete()

        return redirect('listarDocentes')
    else:
        
        users = Docente.objects.all()
        datos = {'docentes': users}
        return render(request, "core/crud_docentes/eliminar_d.html", datos) 


def obtener_detalle_docente(request, rut):
    docente = Docente.objects.get(rut=rut)
    data = {
        'nombre': docente.nombre,
        'email': docente.email,
        'areaAcademica': docente.areaAcademica,
    }
    return JsonResponse(data)





#Vistas Alumnos
def agregarAlumnos(request):                    
    if request.method == 'POST':           
        if request.POST.get('nombre') and request.POST.get('rut') and request.POST.get('carrera') and request.POST.get('email'):
            alumnos = Alumno()
            alumnos.nombre = request.POST.get('nombre')
            alumnos.rut = request.POST.get('rut')
            alumnos.email = request.POST.get('email')
            alumnos.carrera = request.POST.get('carrera')
            alumnos.save()
            return redirect('listarAlumnos')
    else:
        return render(request,"core/crud_alumnos/agregar_a.html") 

def listarAlumnos(request):                    
    return render(request,"core/crud_alumnos/listar_a.html",{ 'alumnos' : Alumno.objects.all()}) 

def actualizarAlumnos(request):
    if request.method == 'POST':
        rut_a_actualizar = request.POST.get('rut')

        # Asegurarse de que el RUT no esté vacío
        if not rut_a_actualizar:
       
            return JsonResponse({'error': 'El RUT no puede estar vacío'})

        try:
            alumno_a_actualizar = Alumno.objects.get(rut=rut_a_actualizar)
        except Alumno.DoesNotExist:
            # Manejar el caso en el que el alumno no existe
            return JsonResponse({'error': 'El alumnono existe'})

        # Resto de tu código para actualizar el alumno
        alumno_a_actualizar.nombre = request.POST.get('nombre')
        alumno_a_actualizar.email = request.POST.get('email')
        alumno_a_actualizar.carrera = request.POST.get('carrera')
        alumno_a_actualizar.save()

        return redirect('listarAlumnos')  # Redirige a la página de listado después de la actualización

    else:
        alumnos = Alumno.objects.all()
        return render(request, "core/crud_alumnos/actualizar_a.html", {'alumnos': alumnos})

def eliminarAlumnos(request):                    
    if request.method == 'POST':
        rut_a_eliminar = request.POST.get('RUT')
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        carrera = request.POST.get('carrera')

        # Recupera la instancia del Alumno que  elimina
        alumno_a_eliminar = Alumno.objects.get(rut=rut_a_eliminar)

        # Elimina 
        alumno_a_eliminar.delete()

        return redirect('listarAlumnos')
    else:
        # Renderiza la página con la información actual de los Alumnos
        users = Alumno.objects.all()
        datos = {'alumnos': users}
        return render(request, "core/crud_alumnos/eliminar_a.html", datos)

def obtener_detalle_alumno(request, rut):
    alumno = Alumno.objects.get(rut=rut)
    data = {
        'nombre': alumno.nombre,
        'email': alumno.email,
        'carrera': alumno.carrera,
    }
    return JsonResponse(data)








#Vistas Cursos

def agregarCursos(request):
    docentes = Docente.objects.all()
 
    context = {
        'docentes': docentes,

    }

    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        docente_id = request.POST.get('docente')
        codigosecc = request.POST.get('codigosecc')

        if codigo and nombre and docente_id and codigosecc:
            # Obtiene o crea el docente
            docente = Docente.objects.get(rut=docente_id)


            # Crea el curso y asigna la sección
            curso = Curso.objects.create(
                codigo=codigo,
                nombre=nombre,
                docente=docente,
                codigosecc=codigosecc,
            )
            curso.codigosecc = codigosecc  # Asigna la sección al curso
            curso.save()

            return redirect('listarCursos')

    return render(request, "core/crud_cursos/agregar_c.html", context)



def listarCursos(request):
    cursos = Curso.objects.all()
    todos_los_alumnos = Alumno.objects.all()  # Asegura de obtener todos los alumnos
    return render(request, "core/crud_cursos/listar_c.html", {'cursos': cursos, 'todos_los_alumnos': todos_los_alumnos})


def actualizarCursos(request):
    if request.method == 'POST':
        id_a_actualizar = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        docente = request.POST.get('docente')
        codigosecc = request.POST.get('codigosecc')
        


        # Recupera la instancia del Beneficio que actualiza
        curso_a_actualizar = Curso.objects.get(codigo=id_a_actualizar)

        # Actualiza los campos del Curso
        curso_a_actualizar.nombre = nombre
        curso_a_actualizar.docente = docente
        curso_a_actualizar.codigosecc = codigosecc
        
        # Actualiza la imagen solo si se proporciona una nueva imagen

        # Guarda los cambios
        curso_a_actualizar.save()

        return redirect('listarCursos')
    else:
        # Renderiza la página con la información actual de los beneficios
        cursos = Curso.objects.all()
        datos = {'cursos': cursos}
        return render(request, "core/crud_cursos/actualizar_c.html", datos)

def eliminarCursos(request):                    
    if request.method == 'POST':
        codigo_a_eliminar = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        docente = request.POST.get('docente')
        codigosecc = request.POST.get('codigosecc')
        # Recupera la instancia del Curso que  actualiza
        codigo_a_eliminar = Curso.objects.get(codigo=codigo_a_eliminar)

        # Elimina los campos del Curso
        codigo_a_eliminar.nombre = nombre
        codigo_a_eliminar.docente = docente
        codigo_a_eliminar.codigosecc = codigosecc
        # Elimina los cambios
        codigo_a_eliminar.delete()

        return redirect('listarCursos')
    else:
        # Renderiza la página con la información actual de los cursos
        users = Curso.objects.all()
        datos = {'cursos': users}
        return render(request, "core/crud_cursos/eliminar_c.html", datos)
    

def obtener_detalle_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    data = {
        'nombre': curso.nombre,
        'docente': curso.docente.nombre,  
        'codigosecc': curso.codigosecc,
    }
    return JsonResponse(data)




def agregar_eliminar_alumnos(request):
    if request.method == 'POST':
        curso_codigo = request.POST.get('curso_codigo')
        curso = Curso.objects.get(codigo=curso_codigo)
        
        # Agregar alumno al curso
        if 'agregar_alumno' in request.POST:
            alumno_rut = request.POST.get('agregar_alumno')
            alumno = Alumno.objects.get(rut=alumno_rut)
            curso.alumnos.add(alumno)
        
        # Eliminar alumno del curso
        eliminar_alumno_rut = request.POST.get('eliminar_alumno')
        if eliminar_alumno_rut:
            alumno = Alumno.objects.get(rut=eliminar_alumno_rut)
            curso.alumnos.remove(alumno)


    return redirect('listarCursos')


#Vistas Beneficios
def agregarBeneficios(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        requisitos = request.POST.get('requisitos')

        # Obtener la imagen del formulario
        imagen = request.FILES.get('imagen')

        if titulo and descripcion and requisitos:
            beneficio = Beneficio(
                titulo=titulo,
                descripcion=descripcion,
                requisitos=requisitos,
                imagen=imagen  # Agrega este campo solo si estás solicitando una imagen
            )
            beneficio.save()
            return redirect('listarBeneficios')
        else:
            print("Formulario incompleto. Asegúrate de que todos los campos obligatorios estén llenos.")
    else:
        return render(request, "core/crud_beneficios/agregar_b.html")


def listarBeneficios(request):             
    beneficios = Beneficio.objects.all()
    print('data', beneficios)
    return render(request, "core/crud_beneficios/listar_b.html", {'beneficios': beneficios})       

def actualizarBeneficios(request):
    if request.method == 'POST':
        id_a_actualizar = request.POST.get('id')
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        requisitos = request.POST.get('requisitos')
        
        # Obtener la imagen del formulario, si se proporciona
        nueva_imagen = request.FILES.get('imagen')

        # Recupera la instancia del Beneficio que  actualizar
        beneficio_a_actualizar = Beneficio.objects.get(id=id_a_actualizar)

        # Actualiza los campos del Beneficio
        beneficio_a_actualizar.titulo = titulo
        beneficio_a_actualizar.descripcion = descripcion
        beneficio_a_actualizar.requisitos = requisitos
        
        # Actualiza la imagen solo si se proporciona una nueva imagen
        if nueva_imagen:
            beneficio_a_actualizar.imagen = nueva_imagen

        # Guarda los cambios
        beneficio_a_actualizar.save()

        return redirect('listarBeneficios')
    else:
        # Renderiza la página con la información actual de los beneficios
        beneficios = Beneficio.objects.all()
        datos = {'beneficios': beneficios}
        return render(request, "core/crud_beneficios/actualizar_b.html", datos)


def eliminarBeneficios(request):                    
    if request.method == 'POST':
        id_a_eliminar = request.POST.get('id')
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        requisitos = request.POST.get('requisitos')
        # Obtener la imagen del formulario
        imagen = request.FILES.get('imagen')

        # Recupera la instancia del Beneficio
        beneficio_a_eliminar = Beneficio.objects.get(id=id_a_eliminar)

        # Elimina los campos del Beneficio
        beneficio_a_eliminar.titulo = titulo
        beneficio_a_eliminar.descripcion = descripcion
        beneficio_a_eliminar.requisitos = requisitos
        beneficio_a_eliminar.imagen = imagen
        # Guarda los cambios
        beneficio_a_eliminar.delete()

        return redirect('listarBeneficios')
    else:
        # Renderiza la página con la información actual de los beneficios
        users = Beneficio.objects.all()
        datos = {'beneficios': users}
                       
        return render(request,"core/crud_beneficios/eliminar_b.html",datos) 


def obtener_detalle_beneficio(request, id):
    beneficio = Beneficio.objects.get(id=id)
    data = {
        'titulo': beneficio.titulo,
        'descripcion': beneficio.descripcion,
        'requisitos': beneficio.requisitos,
        'imagen': beneficio.imagen.url if beneficio.imagen else '',
    }
    return JsonResponse(data)








#Vistas Tótems






def agregarTotems(request):
    # Obtener todos los docentes, cursos y beneficios disponibles
    docentes = Docente.objects.all()
    cursos = Curso.objects.all()
    beneficios = Beneficio.objects.all()

    context = {
        'docentes': docentes,
        'cursos': cursos,
        'beneficios': beneficios,
    }

    if request.method == 'POST':
        # Lógica para guardar el totem con los datos del formulario
        codigo = request.POST.get('codigo')
        motivo = request.POST.get('motivo')
        fecha_expiracion = request.POST.get('fecha_expiracion')
        docente = request.POST.get('docente')
        curso = request.POST.get('curso')
        alumno = request.POST.get('alumno')
        beneficio = request.POST.get('beneficio')
        imagen = request.FILES.get('imagen')

        fecha_creacion = timezone.now()

        if codigo and motivo and fecha_expiracion and docente and curso and alumno and beneficio:
            # Obtener el objeto Curso y Alumno relacionados
            curso_obj = Curso.objects.get(codigo=curso)
            alumno_obj = Alumno.objects.get(rut=alumno)

            # Crear y guardar el objeto Totem
            totem = Totem(
                codigo=codigo,
                motivo=motivo,
                fecha_expiracion=fecha_expiracion,
                docente=Docente.objects.get(rut=docente),
                curso=curso_obj,
                alumno=alumno_obj,
                beneficio=Beneficio.objects.get(id=beneficio),
                fecha_creacion=fecha_creacion,
                imagen=imagen,
            )
            totem.save()

            # Redirigir a la vista 'listarTotems'
            return redirect('listarTotems')

    # En el método GET, obtener los alumnos para el primer curso disponibles
    if cursos:
        primer_curso = cursos[0]
        # Obtener el objeto Curso relacionado
        curso_obj = Curso.objects.get(codigo=primer_curso.codigo)
        # Filtrar los alumnos asociados al curso específico
        alumnos = Alumno.objects.filter(curso=curso_obj)
        context['alumnos'] = alumnos

    return render(request, "core/crud_totems/agregar_t.html", context)



def listarTotems(request):                    
    totems = Totem.objects.all()
    print('data', totems)
    return render(request, "core/crud_totems/listar_t.html", {'totems': totems}) 



def agregarTotemsDocente(request):
    # Obtener todos los docentes, cursos y beneficios disponibles
    docentes = Docente.objects.all()
    cursos = Curso.objects.all()
    beneficios = Beneficio.objects.all()

    context = {
        'docentes': docentes,
        'cursos': cursos,
        'beneficios': beneficios,
    }

    if request.method == 'POST':
        # Lógica para guardar el totem con los datos del formulario
        codigo = request.POST.get('codigo')
        motivo = request.POST.get('motivo')
        docente = request.POST.get('docente')
        curso = request.POST.get('curso')
        alumno = request.POST.get('alumno')
        beneficio = request.POST.get('beneficio')
        imagen = request.FILES.get('imagen')  # Cambiado para obtener archivos correctamente

        # Asegúrate de que 'fecha_creacion' esté en tu formulario o define su valor aquí
        fecha_creacion = timezone.now()

        if codigo and motivo and docente and curso and alumno and beneficio and fecha_creacion:
            # Obtener el objeto Curso y Alumno relacionados
            curso_obj = Curso.objects.get(codigo=curso)
            alumno_obj = Alumno.objects.get(rut=alumno)

            # Crear y guardar el objeto Totem
            totem = Totem(
                codigo=codigo,
                motivo=motivo,
                docente=Docente.objects.get(rut=docente),
                curso=curso_obj,
                alumno=alumno_obj,
                beneficio=Beneficio.objects.get(id=beneficio),
                fecha_creacion=fecha_creacion,
                imagen=imagen,  # Asignar el objeto de archivo directamente
            )
            totem.save()

            # Redirigir a la vista 'listarTotems'
            return redirect('diseno')

    # En el método GET, obtener los alumnos para el primer curso disponibles
    if cursos:
        primer_curso = cursos[0]
        # Obtener el objeto Curso relacionado
        curso_obj = Curso.objects.get(codigo=primer_curso.codigo)
        # Filtrar los alumnos asociados al curso específico
        alumnos = Alumno.objects.filter(curso=curso_obj)
        context['alumnos'] = alumnos

    return render(request, "core/diseno.html", context)

def actualizarTotems(request):
    if request.method == 'POST':
        id_a_actualizar = request.POST.get('codigo')
        motivo = request.POST.get('motivo')
        fecha_expiracion = request.POST.get('fecha_expiracion')
        docente = request.POST.get('docente')
        alumno = request.POST.get('alumno')
        beneficio = request.POST.get('beneficio')
        curso = request.POST.get('curso')

        # Obtener la imagen del formulario, si se proporciona
        nueva_imagen = request.FILES.get('imagen')

        # Recupera la instancia del Totem a actualizar
        totem_a_actualizar = Totem.objects.get(codigo=id_a_actualizar)

        # Actualiza los campos del Totem
        totem_a_actualizar.motivo = motivo
        totem_a_actualizar.fecha_expiracion = fecha_expiracion
        totem_a_actualizar.docente = docente
        totem_a_actualizar.alumno = alumno
        totem_a_actualizar.beneficio = beneficio
        totem_a_actualizar.beneficio = curso

        # Actualiza la imagen solo si se proporciona una nueva imagen
        if nueva_imagen:
            totem_a_actualizar.imagen = nueva_imagen

        # Guarda los cambios
        totem_a_actualizar.save()

        return redirect('listarTotems')
    else:
        # Renderiza la página con la información actual de los totems
        totems = Totem.objects.all()
        datos = {'totems': totems}
        return render(request, "core/crud_totems/actualizar_t.html", datos)


def eliminarTotems(request):                 
    if request.method == 'POST':
        id_a_eliminar = request.POST.get('id')
        motivo = request.POST.get('motivo')
        fecha_expiracion = request.POST.get('fecha_expiracion')
        fecha_creacion = request.POST.get('fecha_creacion')
        docente = request.POST.get('docente')
        alumno = request.POST.get('alumno')
        beneficio = request.POST.get('beneficio')
        curso = request.POST.get('curso')
        imagen = request.FILES.get('imagen')

        # Recupera la instancia del Totem
        totem_a_eliminar = Totem.objects.get(codigo=id_a_eliminar)

        # Elimina los campos del Totem
        totem_a_eliminar.motivo = motivo
        totem_a_eliminar.fecha_expiracion = fecha_expiracion
        totem_a_eliminar.docente = docente
        totem_a_eliminar.imagen = imagen
        totem_a_eliminar.alumno = alumno
        totem_a_eliminar.beneficio = beneficio
        totem_a_eliminar.imagen = imagen
        totem_a_eliminar.fecha_creacion = fecha_creacion
        totem_a_eliminar.curso = curso

        totem_a_eliminar.delete()

        return redirect('listarTotems')
    else:
        # Renderiza la página con la información actual de los Totem
        users = Totem.objects.all()
        datos = {'totems': users}
                       
        return render(request,"core/crud_totems/eliminar_t.html",datos) 


def obtener_detalle_totem(request, codigo):
    totem = Totem.objects.get(codigo=codigo)
    data = {
        'imagen': totem.imagen.url if totem.imagen else '',
        'motivo': totem.motivo,
        'fecha_creacion': totem.fecha_creacion,
        'fecha_expiracion': totem.fecha_expiracion,
        'fecha_creacion': totem.fecha_creacion,
        'docente': totem.docente,
        'alumno': totem.alumno,
        'beneficio': totem.beneficio,
        'curso': totem.curso,

    }
    return JsonResponse(data)



def validar_totem(request):
    if request.method == 'POST':
        form = TotemValidationForm(request.POST)
        if form.is_valid():
            # Combinación de las tres partes del código
            totem_code = f"{form.cleaned_data['code_part1']}-{form.cleaned_data['code_part2']}-{form.cleaned_data['code_part3']}"


            try:
                totem = Totem.objects.get(codigo=totem_code)
                print(totem.__dict__)  # Imprime los datos del tótem
                return render(request, 'core/index.html', {'totem_data': totem})
            except Totem.DoesNotExist:
                print('Totem not found')  # Imprime un mensaje en la consola para verificar
                return render(request, 'core/index.html', {'error_message': 'Totem not found'})

    else:
        form = TotemValidationForm()

    return render(request, 'core/index.html', {'form': form})






