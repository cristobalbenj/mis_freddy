from django.urls import path
from django.conf import settings
from django.contrib import admin
from .views import home,galeria,formulario,agregar_mascota,listar_mascotas,eliminar_mascota,modificar_mascota,crearusuario
 
urlpatterns = [
    path('', home,name="home"),
    path('galeria/', galeria,name="galeria"),
    path('formulario/', formulario,name="formulario"),
    path('agregar-mascota/', agregar_mascota,name="agregar_mascota"), 
    path('listar-mascotas/', listar_mascotas,name="listar_mascotas"), 
    path('eliminar-mascota/<id>/', eliminar_mascota,name="eliminar_mascota"), 
    path('modificar-mascota/<id>/', modificar_mascota,name="modificar_mascota"),
    path('crearusuario', crearusuario,name="crearusuario"),
]
