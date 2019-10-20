from django.shortcuts import render
from .models import Usuario, Testimonio, Consulta

# Create your views here.
def index(request):
	return render(request, 'home.html')

def inputs(request):
	return render(request, 'inputs.html')

def inicio(request):
	return render(request, 'inicio.html')

def creacion(request):
	return render(request, 'creacion.html')

def contacto(request):
	return render(request, 'contacto.html')		

def testimonios(request):
	return render(request, 'testimonios.html')		

def exitocreacion(request):
	return render(request, 'exitocreacion.html')

def exitoinicio(request):
	return render(request, 'exitoinicio.html')

def exitoinputs(request):
	return render(request, 'exitoinputs.html')


def cuenta(request):
	#guarda la información de la cuenta creada
	nombre = request.POST['nombre']
	correo = request.POST['correo']
	contraseña = request.POST['contraseña']
	edad = request.POST['edad']
	diccionario = {}
	diccionario["comentario"]=nombre
	diccionario["comentario2"]= correo
	diccionario["comentario3"] = contraseña
	diccionario["comentario4"]=edad
	usuario=Usuario(nombre=nombre, correo=correo, contrasena=contraseña, edad=edad)
	usuario.save()
	return render(request, "exitocreacion.html", diccionario)

def iniciar(request):
	return render(request, "exitoinicio.html")

def consulta(request):
	nombre = request.POST['inputText']
	detalle = request.POST['detalle']
	numero = request.POST['inputNumber']
	fecha = request.POST['inputDate']
	correo = request.POST['inputEmail']
	camion = request.POST['inputCarrera']
	foto = request.POST['foto']
	consulta=Consulta(nombre=nombre,detalle=detalle,numero=numero,fecha=fecha,correo=correo,camion=camion,foto=foto)
	consulta.save()
	return render(request, "exitoinputs.html")

def exitotestimonio(request):
	return render(request, 'exitotestimonio.html')

def guardar(request):
	nombre = request.POST['inputText']
	correo = request.POST['inputEmail']
	comentario = request.POST['comentario']
	testimonio=Testimonio(nombre=nombre, correo=correo, testimonio=comentario)
	testimonio.save()
	return render(request, "exitotestimonio.html")