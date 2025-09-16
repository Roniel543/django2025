from django.shortcuts import render
# El metodo de render es renderizar -> basicamente convierte code backend aqui y lo retorna el html y el server renderiza el resultado y lo entrega en template

# Create your views here.


def index(request):
    listaArticulos = [
        {
            "title": "Curso: Programación orientada a objetos con JavaScript",
            "image": "https://edteam-media.s3.amazonaws.com/courses/big/cbe73fb7-2693-4e9c-a6c5-6cdd94b695e0.png",
            "summary": "Implementa el paradigma de programación más utilizado en JavaScript.",
            "author": "Beto Quiroga",
        },
        {
            "title": "Ocelot, el chip cuántico de Amazon ¡90% más eficiente que Google!",
            "image": "https://edteam-media.s3.amazonaws.com/blogs/original/6ec875b8-e114-403e-8892-86d6aa594422.jpeg",
            "summary": "Amazon acaba de presentar su primer chip cuántico y promete ser un cambio de juego en la computación cuántica. Pero, ¿qué lo hace diferente de las propuestas de Google y Microsoft?.",
            "author": "Alvaro Felipe Chávez",
        },
        {
            "title": "Majorana 1 de Microsoft: la clave para el futuro de la computación cuántica",
            "image": "https://edteam-media.s3.amazonaws.com/blogs/original/8b289e2e-d1c9-4861-b46f-c48d68dfd1e0.jpeg",
            "summary": "Microsoft ha anunciado un avance significativo en la computación cuántica que podría dejar obsoleta la tecnología actual. Descubre cómo esta revolución tecnológica promete cambiar el futuro.",
            "author": "Alvaro Felipe Chávez",
        }
    ]

    context = {
        "articulos" : listaArticulos
    }

    return render(request, 'index.html', context)
