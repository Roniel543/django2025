from email.policy import default
from random import choices
from django.utils import timezone
from unicodedata import category
from django.db import models
from datetime import date

# Create your models here.
class Articulo(models.Model):

    CATEGORIA_CHOICES = (
        ('general','General'),
        ('diseño web','Diseño Web'),
        ('programación','Programación')
    )

    title = models.CharField(max_length=200)
    contenido = models.TextField(default='')
    duracion = models.IntegerField(default=0)
    fecha_registro = models.DateField(default=date.today)
    categoria = models.CharField(max_length=50,default='general', choices = CATEGORIA_CHOICES)
    image = models.ImageField(upload_to='articulos',blank=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    texto = models.TextField(default='')
    autor = models.CharField(max_length=255, default='anónimo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.autor