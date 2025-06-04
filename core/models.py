from django.db import models




class Docente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    areaAcademica = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rut} - {self.nombre}"
    
class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    carrera = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.rut} - {self.nombre}"
    


    
class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    codigosecc = models.CharField(max_length=20, unique=True)
    alumnos = models.ManyToManyField(Alumno, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.codigo} - {self.docente} - {self.codigosecc} - {self.codigosecc}"









# Modelo de Beneficio
class Beneficio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    requisitos = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='static/core/img/beneficios/', null=True, blank=True)  

    def __str__(self):
        return f"{self.titulo} - {self.descripcion} - {self.requisitos}"
    
# Modelo de Tótem
class Totem(models.Model):
    codigo = models.CharField(primary_key=True, max_length=9)
    imagen = models.ImageField(upload_to='static/core/img/totems/')
    motivo = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_expiracion = models.DateTimeField()
    docente = models.ForeignKey('Docente', on_delete=models.CASCADE)
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)

    beneficio = models.ForeignKey('Beneficio', on_delete=models.CASCADE)    

    def __str__(self):
            return f"{self.codigo} - {self.alumno} - {self.fecha_creacion} - {self.beneficio} - {self.fecha_expiracion} - {self.curso} - {self.docente}"

    









