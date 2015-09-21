from django.db import models
 

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
	imagen = models.ImageField(upload_to = 'fotos_lugar')
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

