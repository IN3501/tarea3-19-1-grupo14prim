from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre=models.CharField(max_Lenght=45)
	correo=models.EmailField(max_Lenght=100)
	contrasena=models.CharField(max_Lenght=45)
	edad=models.IntegerField()

class Testimonio(models.Model):
	nombre=models.CharField(max_Lenght=45)
	correo=models.EmailField(max_Lenght=100)
	testimonio=models.CharField(max_Lenght=512)
	usuario=models.ForeingKey(Usuario, on_delete=models.CASCADE)

class Consulta(models.Model):
	nombre=models.CharField(max_Lenght=45)
	detalle=models.CharField(max_Lenght=512)
	numero=models.IntegerField()
	fecha=models.DateField()
	correo=models.EmailField(100)
	camion=models.CharField(max_Lenght=45)
	foto=models.FileField(upload_to='uploads/')
	usuario=models.ForeingKey(Usuario, on_delete=models.CASCADE)