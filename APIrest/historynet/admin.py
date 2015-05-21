from django.contrib import admin
from .models import Usuario, Lugar, Informacion_adicional, Comentario, Lugares_favoritos, Valoraciones_comentarios, Valoraciones_info_adicional, Valoraciones_lugar

class LugarAdmin(admin.ModelAdmin):
	#list_display = ('nombre','informacion_primaria','imagen_lugar')
	list_display = ('id','nombre','informacion_primaria','latitud','longitud','estado')

	#def imagen_lugar(self, lugar):
	#	url = lugar.url_imagen()
	#	tag = "<img src='%s' >" % url
	#	return tag

	#imagen_lugar.allow_tags = True

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('id','user_name','password','nombre','apellido','level','estado')

class Informacion_adicionalAdmin(admin.ModelAdmin):
	list_display = ('id','lugar_id','mensaje','estado')

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('id','user_id','lugar_id','mensaje','estado')

class Lugares_favoritosAdmin(admin.ModelAdmin):
	list_display = ('id','user_id','lugar_id')

class Valoraciones_comentariosAdmin(admin.ModelAdmin):
	list_display = ('id','user_id','comentario_id','valoracion')

class Valoraciones_info_adicionalAdmin(admin.ModelAdmin):
	list_display = ('id','user_id','info_adicional_id','valoracion')

class Valoraciones_lugarAdmin(admin.ModelAdmin):
	list_display = ('id','user_id','lugar_id','valoracion')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Informacion_adicional, Informacion_adicionalAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Lugares_favoritos, Lugares_favoritosAdmin)
admin.site.register(Valoraciones_comentarios, Valoraciones_comentariosAdmin)
admin.site.register(Valoraciones_lugar, Valoraciones_lugarAdmin)
admin.site.register(Valoraciones_info_adicional, Valoraciones_info_adicionalAdmin)
