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
	user_name = models.CharField(max_length = 50, unique = True)
	password = models.CharField(max_length = 50)
	email = models.CharField(max_length = 100)
	nombre = models.CharField(max_length = 150)
	apellido = models.CharField(max_length = 150)
	pais = models.CharField(max_length = 15)
	sexo = models.CharField(max_length = 1)
	level = models.SmallIntegerField(default = 0)
	estado = models.SmallIntegerField(default = 1)
	last_login = models.DateTimeField(auto_now = True)
	
	def get_full_name(self):
		return (self.nombre + " " + self.apellido)

	def __unicode__(self):
		return self.user_name

	class Meta:
		ordering = ('user_name',)


class Lugar(models.Model):
	nombre = models.CharField(max_length = 150)
	direccion = models.CharField(max_length = 1024)
	informacion_primaria = models.CharField(max_length = 1024)
	longitud = models.FloatField()
	latitud = models.FloatField()
	#imagen = models.ImageField(upload_to = 'foto_lugar')
	fecha = models.DateTimeField(auto_now_add = True)
	valoracion = models.FloatField(default = 0)
	denuncia = models.IntegerField(default = 0)
	estado = models.SmallIntegerField(default = 2) # Un lugar debe ser validado por un administrador
	a_distancia_b = models.FloatField(default = 0)
	#def url_imagen(self):
	#	return 'http://46.101.184.198:8000/media/%s' % self.imagen

	def __unicode__(self):
		return self.nombre

	class Meta:
		ordering = ('nombre',)


class Informacion_adicional(models.Model):
	lugar_id = models.ForeignKey(Lugar) #relacion 1 a muchos entre lugar e informacion add
	mensaje = models.CharField(max_length = 1024)
	fecha = models.DateTimeField(auto_now_add = True)
	denuncia = models.IntegerField(default = 0)
	estado = models.SmallIntegerField(default = 2) # Una informacion adicional debe ser validada por un administrador
	
	def __unicode__(self):
		return self.mensaje

	class Meta:
		ordering = ('fecha',)


class Comentario(models.Model):
	user_id = models.ForeignKey(Usuario) #relacion entre usuario y comentario (un user puede hacer varios comentarios)
	lugar_id = models.ForeignKey(Lugar) #relacion entre lugar y comentario (Un lugar puede tener varios comentarios)
	mensaje = models.CharField(max_length = 1024)
	fecha = models.DateTimeField(auto_now_add = True)
	valoracion = models.FloatField(default = 0)
	denuncia = models.IntegerField(default = 0)
	estado = models.SmallIntegerField(default = 1)

	def __unicode__(self):
		return self.mensaje

	class Meta:
		ordering = ('fecha',)


class Lugares_favoritos(models.Model):
	user_id = models.ForeignKey(Usuario) #relacion n a n entre lugares y usuarios para registro de favoritos
	lugar_id = models.ForeignKey(Lugar)

class Valoraciones_comentarios(models.Model):
	user_id = models.ForeignKey(Usuario) #relacion 1 a 1 entre usuario y comentario para registro de valoracion
	comentario_id = models.ForeignKey(Comentario)
	valoracion = models.IntegerField()

class Valoraciones_info_adicional(models.Model):
	user_id = models.ForeignKey(Usuario) #relacion 1 a 1 entre usuario e info add para registro de valoracion
	info_adicional_id = models.ForeignKey(Informacion_adicional)
	valoracion = models.IntegerField()

class Valoraciones_lugar(models.Model):
	user_id = models.ForeignKey(Usuario) #relacion 1 a 1 entre usuario y lugar para registro de valoracion
	lugar_id = models.ForeignKey(Lugar)
	valoracion = models.IntegerField()

