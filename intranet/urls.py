from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.login,name="login"),
    path('diseno/', views.diseno,name="diseno"),
    path('admin/', admin.site.urls),
    
    
    path('fablab/', views.index, name="index"),
    path('agregarDocentes/', views.agregarDocentes,name="agregarDocentes"),
    path('listarDocentes/', views.listarDocentes,name="listarDocentes"),
    path('actualizarDocentes/', views.actualizarDocentes,name="actualizarDocentes"),
    path('eliminarDocentes/', views.eliminarDocentes,name="eliminarDocentes"),

    path('agregarAlumnos/', views.agregarAlumnos,name="agregarAlumnos"),
    path('listarAlumnos/', views.listarAlumnos,name="listarAlumnos"),
    path('actualizarAlumnos/', views.actualizarAlumnos,name="actualizarAlumnos"),
    path('eliminarAlumnos/', views.eliminarAlumnos,name="eliminarAlumnos"),

    path('agregarCursos/', views.agregarCursos,name="agregarCursos"),
    path('listarCursos/', views.listarCursos,name="listarCursos"),
    path('actualizarCursos/', views.actualizarCursos,name="actualizarCursos"),
    path('eliminarCursos/', views.eliminarCursos,name="eliminarCursos"),

    path('agregarBeneficios/', views.agregarBeneficios,name="agregarBeneficios"),
    path('listarBeneficios/', views.listarBeneficios,name="listarBeneficios"),
    path('actualizarBeneficios/', views.actualizarBeneficios,name="actualizarBeneficios"),
    path('eliminarBeneficios/', views.eliminarBeneficios,name="eliminarBeneficios"),

    path('agregarTotems/', views.agregarTotems,name="agregarTotems"),
    path('agregarTotemsDocente/', views.agregarTotemsDocente,name="agregarTotemsDocente"),

    path('listarTotems/', views.listarTotems,name="listarTotems"),
    path('actualizarTotems/', views.actualizarTotems,name="actualizarTotems"),
    path('eliminarTotems/', views.eliminarTotems,name="eliminarTotems"),


    path('obtener_detalle_docente/<str:rut>/', views.obtener_detalle_docente, name='obtener_detalle_docente'),
    path('obtener_detalle_beneficio/<int:id>/', views.obtener_detalle_beneficio, name='obtener_detalle_beneficio'),
    path('obtener_detalle_alumno/<str:rut>/', views.obtener_detalle_alumno, name='obtener_detalle_alumno'),
    path('obtener_detalle_curso/<str:codigo>/', views.obtener_detalle_curso, name='obtener_detalle_curso'),
    path('obtener_detalle_totem/<str:codigo>/', views.obtener_detalle_totem, name='obtener_detalle_totem'),
    path('agregar_eliminar_alumnos/', views.agregar_eliminar_alumnos, name='agregar_eliminar_alumnos'),
    path('validar_totem/', views.validar_totem, name='validar_totem'),
]