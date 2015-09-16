models.py

Un modelo es la única fuente de información sobre su base de datos.
Contiene los campos esencialesy los comportamientos de los datos que se está almacenando.
En general, cada modelo se asigna a una sola tabla de base datos.
Cada modelo es una clase Python que hereda de django.db.models.Model
Cada atributo del modelo representa un campo de base de datos.
Con todo esto, Django proporciona una API de base de datos generada automáticamente.

# Falta CS-014, CS-018 , CS-021, CS-022 en el modelado de database.
# http://prntscr.com/75azso

from django.db import models
 
# El campo "level" representa jerarquia de usuario (el numero de cada uno es solo una idea)
# 0 = usuario normal
# 1 = super usuario (ideas pero nada especial)
# 4 = moderador (ideas pero nada especial)
# 5 = administrador


# El campo "estado" tiene distintos valores de representacion:
# 0 = desactivado por usuario (only login)
# 1 = habilitado
# 2 = en pedido de habilitacion
# 3 = bloqueado por admin


class Usuario(models.Model):
	user_name = models.CharField(max_length = 24, unique = True)
	password = models.CharField(max_length = 24)
	email = models.CharField(max_length = 50)
	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50)
	sexo = models.CharField(max_length = 1)
	pais = models.CharField(max_length = 20)
	ciudad = models.CharField(max_length = 20)
	level = models.SmallIntegerField(default = 0)
	estado = models.SmallIntegerField(default = 1)
	
	def get_full_name(self):
		return (self.nombre + " " + self.apellido)

	def __unicode__(self):
		return self.user_name

	class Meta:
		ordering = ('user_name',)


class Lugar(models.Model):
	nombre = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 200)
	informacion_primaria = models.CharField(max_length = 1024)
	latitud = models.FloatField()
	longitud = models.FloatField()
	tag = models.CharField(max_length = 1024)
	fecha = models.DateTimeField(auto_now_add = True)
	cant_valoracion = models.IntegerField(default = 0)
	prom_valoracion = models.FloatField(default = 0)
	denuncia = models.IntegerField(default = 0)
	estado = models.SmallIntegerField(default = 2)
	a_distancia_b = models.FloatField(default = 0)
	
	def __unicode__(self):
		return self.nombre

	class Meta:
		ordering = ('fecha',)


class Informacion_adicional(models.Model):
	lugar_id = models.ForeignKey(Lugar) 
	mensaje = models.CharField(max_length = 1024)
	fecha = models.DateTimeField(auto_now_add = True)
	cant_valoracion = models.IntegerField(default = 0)
	prom_valoracion = models.FloatField(default = 0)
	denuncia = models.IntegerField(default = 0)
	estado = models.SmallIntegerField(default = 2)
	
	def __unicode__(self):
		return self.mensaje

	class Meta:
		ordering = ('fecha',)


class Comentario(models.Model):
	user_id = models.ForeignKey(Usuario)
	lugar_id = models.ForeignKey(Lugar)
	mensaje = models.CharField(max_length = 1024)
	fecha = models.DateTimeField(auto_now_add = True)
	cant_valoracion = models.IntegerField(default = 0)
	prom_valoracion = models.FloatField(default = 0)
	denuncia = models.IntegerField(default = 0)
	estado = models.SmallIntegerField(default = 1)

	def __unicode__(self):
		return self.mensaje

	class Meta:
		ordering = ('fecha',)


class Lugares_favoritos(models.Model):
	user_id = models.ForeignKey(Usuario) 
	lugar_id = models.ForeignKey(Lugar)

class Valoraciones_comentarios(models.Model):
	user_id = models.ForeignKey(Usuario) 
	comentario_id = models.ForeignKey(Comentario)
	valoracion = models.IntegerField()

class Valoraciones_info_adicional(models.Model):
	user_id = models.ForeignKey(Usuario) 
	info_adicional_id = models.ForeignKey(Informacion_adicional)
	valoracion = models.IntegerField()

class Valoraciones_lugar(models.Model):
	user_id = models.ForeignKey(Usuario) 
	lugar_id = models.ForeignKey(Lugar)
	valoracion = models.IntegerField()

