from django.shortcuts import render

# Create your views here.
def ejemplo(request):
    return render(request, 'miapp/pagina.html')

def otra(request):
    return render(request, 'miapp/sidebar.html')