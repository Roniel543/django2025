from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo
# El metodo de render es renderizar -> basicamente convierte code backend aqui y lo retorna el html y el server renderiza el resultado y lo entrega en template

# Create your views here.

def hola_mundo(request):
    return HttpResponse('<h1>Hola Mundo</h1>')

def index(request):

    #articulos = Articulo.objects.all()

    listaArticulos = Articulo.objects.all()
    print(listaArticulos)



    context = {
        ##Aqui lo que viaja es la variable articulos el cual puedo acceder a ese tambien 
        "articulos" : listaArticulos
    }
    return render(request, 'blog/index.html',context)

def detalle_Articulo(request,articulo_id):
    objArticulo = Articulo.objects.get(pk=articulo_id)
    
    contex = {
        "articulo": objArticulo
    }

    return render(request,'blog/articulo.html',contex)