from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('contenido/<int:articulo_id>/', views.detalle_Articulo, name='contenido'),
    path('comentar/<int:articulo_id>/', views.comentar, name='comentar'),
]