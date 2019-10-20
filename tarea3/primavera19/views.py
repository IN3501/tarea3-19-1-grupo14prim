from django.shortcuts import render

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

def cuenta(request):
	#guarda la información de la cuenta creada
	usuario = request.POST['usuario']
	correo = request.POST['correo']
	contraseña = request.POST['contraseña']
	edad = request.POST['edad']
	diccionario = {}
	diccionario["comentario"]=usuario
	diccionario["comentario2"]= correo
	diccionario["comentario3"] = contraseña
	diccionario["comentario4"]=edad
	return render(request, "exitocreacion.html", diccionario)

def iniciar(request):
	return render(request, "exitoinicio.html")

def consulta(request):
	return render(request, "exitoinputs.html")

def guardar(request):
	return render(request, "exitotestimonio.html")