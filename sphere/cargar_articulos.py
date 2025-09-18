import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sphere.settings')
django.setup()
from blog.models import Articulo

articulos = [
    {'title' : 'Articulo 5','image' : 'image10.jpg','author':'author10'},
    {'title' : 'Articulo 6','image' : 'image10.jpg','author':'author10'},
    {'title' : 'Articulo 7','image' : 'image10.jpg','author':'author10'},
]

for data in articulos:
    Articulo.objects.create(**data)
print("ESTAS APRENDIEND DJANGO DE LA MEJOR MANERA, ARTICULOS CREADOS")