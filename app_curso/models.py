from django.db import models

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=50)
    descripcion = models.TextField()
    duracion_semanas = models.IntegerField()
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    numero_estudiantes = models.IntegerField()

    def __str__(self):
        return f'Curso: {self.nombre_curso} {self.descripcion} {self.duracion_semanas} {self.costo} {self.numero_estudiantes}'
