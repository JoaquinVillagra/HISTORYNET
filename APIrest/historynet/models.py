# Falta CS-014 , CS-021, CS-022 en el modelado de database.
# http://prntscr.com/75azso

from django.db import models


class Login(models.Model):
	user_name = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	email = models.CharField(max_length = 100)
	level = models.SmallIntegerField()
	estado = models.SmallIntegerField()
	last_login = models.DateTimeField(auto_now = True)

class Usuario(models.Model):
	login = models.OneToOneField(Login, primary_key=True) #relacion 1 a 1 entre login y usuario
	nombre = models.CharField(max_length = 150)
	apellido = models.CharField(max_length = 150)
	pais = models.CharField(max_length = 15)
	sexo = models.CharField(max_length = 1)

class Lugar(models.Model):
	nombre = models.CharField(max_length = 150)
	direccion = models.CharField(max_length = 1024)
	informacion_primaria = models.CharField(max_length = 1024)
	longitud = models.FloatField()
	latitud = models.FloatField()
	fecha = models.DateTimeField(auto_now_add = True)
	valoracion = models.FloatField()
	denuncia = models.IntegerField()
	estado = models.SmallIntegerField()

class Informacion_adicional(models.Model):
	lugar_id = models.ForeignKey(Lugar) #relacion 1 a muchos entre lugar e informacion add
	mensaje = models.CharField(max_length = 1024)
	fecha = models.DateTimeField(auto_now_add = True)
	denuncia = models.IntegerField()
	estado = models.SmallIntegerField()

class Comentario(models.Model):
	user_id = models.ForeignKey(Usuario) #relacion entre usuario y comentario (un user puede hacer varios comentarios)
	lugar_id = models.ForeignKey(Lugar) #relacion entre lugar y comentario (Un lugar puede tener varios comentarios)
	mensaje = models.CharField(max_length = 1024)
	fecha = models.DateTimeField(auto_now_add = True)
	valoracion = models.FloatField()
	denuncia = models.IntegerField()
	estado = models.SmallIntegerField()

class Lugares_favoritos(models.Model):
	user_id = models.ManyToManyField(Login) #relacion n a n entre lugares y usuarios para registro de favoritos
	lugar_id = models.ManyToManyField(Lugar)

class Valoraciones_comentarios(models.Model):
	user_id = models.OneToOneField(Login) #relacion 1 a 1 entre usuario y comentario para registro de valoracion
	comentario_id = models.OneToOneField(Comentario)
	valoracion = models.IntegerField()

class Valoraciones_info_adicional(models.Model):
	user_id = models.OneToOneField(Login) #relacion 1 a 1 entre usuario e info add para registro de valoracion
	info_adicional_id = models.OneToOneField(Informacion_adicional)
	valoracion = models.IntegerField()

class Valoraciones_lugar(models.Model):
	user_id = models.OneToOneField(Login) #relacion 1 a 1 entre usuario y lugar para registro de valoracion
	lugar_id = models.OneToOneField(Lugar)
	valoracion = models.IntegerField()

