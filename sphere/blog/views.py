from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Articulo, Comentario

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

def detalle_Articulo(request, articulo_id):
    objArticulo = Articulo.objects.get(pk=articulo_id)
    listaComentarios = Comentario.objects.filter(articulo=objArticulo)
    
    context = {
        "articulo": objArticulo,
        "comentarios": listaComentarios
    }

    return render(request, 'blog/articulo.html', context)

def comentar(request, articulo_id):
    if request.method == 'POST':
        objArticulo = Articulo.objects.get(pk=articulo_id)
        comentario = request.POST.get('comentario')
        autor = request.POST.get('autor', 'Anónimo')
        
        print(f"Comentario: {comentario}")
        print(f"Autor: {autor}")
        
        nuevo_comentario = Comentario()
        nuevo_comentario.texto = comentario
        nuevo_comentario.autor = autor
        nuevo_comentario.articulo = objArticulo
        nuevo_comentario.save()
    
    return redirect('contenido', articulo_id=articulo_id)