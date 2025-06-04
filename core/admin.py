from django.contrib import admin
from .models import Docente
from .models import Alumno
from .models import Curso
from .models import Beneficio
from .models import Totem



# Register your models here.


admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Beneficio)
admin.site.register(Totem)


