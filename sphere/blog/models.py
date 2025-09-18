from django.db import models

# Create your models here.
class Articulo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articulos',blank=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    