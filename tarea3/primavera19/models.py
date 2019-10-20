from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre=models.CharField(max_lenght=45)
	correo=models.EmailField(max_lenght=100)
	contrasena=models.CharField(max_lenght=45)
	edad=models.IntegerField()

class Testimonio(models.Model):
	nombre=models.CharField(max_lenght=45)
	correo=models.EmailField(max_lenght=100)
	testimonio=models.CharField(max_lenght=512)
	usuario=models.ForeingKey(Usuario, on_delete=models.CASCADE)

class Consulta(models.Model):
	nombre=models.CharField(max_lenght=45)
	detalle=models.CharField(max_lenght=512)
	numero=models.IntegerField()
	fecha=models.DateField()
	correo=models.EmailField(max_lenght=100)
	camion=models.CharField(max_lenght=45)
	foto=models.FileField(upload_to='uploads/')
	usuario=models.ForeingKey(Usuario, on_delete=models.CASCADE)