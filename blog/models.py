from django.db import models
from django.utils import timezone

class Publicar(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
                default=timezone.now)
    fecha_publica = models.DateTimeField(
                blank=True, null=True)

    def publicacion(self):
        self.fecha_publica = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
# Create your models here.
