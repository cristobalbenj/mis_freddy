from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Mascota,Raza,Genero,Estado,tipoVivienda,GeneroP,Region,Ciudad,Persona
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    return render(request,'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def formulario(request):
    persona = Persona.objects.all()
    vivienda = tipoVivienda.objects.all()
    sexoo = GeneroP.objects.all()
    region = Region.objects.all()
    ciudad = Ciudad.objects.all()

    variables = {

        'persona' : persona,
        'vivienda' : vivienda,
        'sexoo' : sexoo,
        'region' : region,
        'ciudad' : ciudad,
    }

    if request.POST:
        persona = Persona()
        persona.correo = request.POST.get('txtCorreo')
        persona.run = request.POST.get('txtRun')
        persona.nombreP = request.POST.get('txtN')
        persona.telefono = request.POST.get('txtTelefono')
        persona.fechaN = request.POST.get('txtFecha')
        persona.direccion = request.POST.get('txtDireccion')

    #   sexo = GeneroP()
    #  sexo.id = request.POST.get('cboGenero')
    #  persona.sexoo = sexo
       
    #  regionT = Region()
    #  regionT.id = request.POST.get('cboRegion')
    #  persona.region = regionT
       
    #  ciudadd = Ciudad()
    #  ciudadd.id = request.POST.get('cbocuidad')
    #   persona.ciudad = ciudadd

    #   tipoV = tipoVivienda()
    #   tipoV.id = request.POST.get('cboVivienda')
    #   persona.vivienda = tipoV


    return render(request, 'core/formulario.html',variables)

@login_required
def agregar_mascota(request):

    perri = Raza.objects.all()
    sexo = Genero.objects.all()
    estado = Estado.objects.all()
    raza = Raza.objects.all()
    variables = {
        'perri':perri,
        'sexo':sexo,
        'estado':estado,
        'raza': raza,
    }


    if request.POST:
        perro = Mascota()
        perro.nombre = request.POST.get('txtNombre')

        razita = Raza()
        razita.id = request.POST.get('cboRaza')
        perro.raza = razita

        sexo = Genero()
        sexo.id = request.POST.get('cboGenero')
        perro.genero = sexo

        perro.fechaIngreso = request.POST.get('txtFechaI')

        if request.POST.get('txtFechaN') != '':
            perro.fechaNacimiento = request.POST.get('txtFechaN')

        perro.imagen = request.POST.get('txtFoto')

        estadito = Estado()
        estadito.id = request.POST.get('cboEstado')
        perro.estado = estadito

        perro.razita = Mascota
        perro.sexo = Mascota
        perro.estadito = Mascota
        perro.save()

        try:

            variables['mensaje'] = 'Guardado Correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/agregar_mascota.html',variables)

#crud mascotas

def listar_mascotas(request):

    mascotas = Mascota.objects.all()

    return render(request,'core/listar_mascotas.html',{
        'mascotas':mascotas 
    })


def eliminar_mascota(request,id):
    #buscar la mascota que deseamos eliminar
    mascota = Mascota.objects.get(id=id)

    try:
        mascota.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request,mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request,mensaje)

    return redirect('listar_mascotas')


def modificar_mascota(request, id):
    #buscamos el id de la mascota
    mascota = Mascota.objects.get(id=id)
    estado = Estado.objects.all()
    raza = Raza.objects.all()
    sexo = Genero.objects.all()
    variables = {
        'mascota': mascota,
        'estado' : estado,
        'raza' : raza,
        'sexo' : sexo,
    }
    
    return render(request, 'core/modificar_mascota.html', variables)

def crearusuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render(request, 'core/crearusuario.html', {'formulario':formulario})