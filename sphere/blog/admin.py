from django.contrib import admin

# Register your models here.
from .models import Articulo

#admin.site.register(Articulo)

#Forma Moderna
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('title','image','author')