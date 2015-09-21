#admin.py Se definen que modelos son mostrados en la sección de Administración default que implementa django. 
#Este puede ser usado para testear los diferentes modelos.

from django.contrib import admin
from .models import Usuario, Lugar, Informacion_adicional, Comentario, Lugares_favoritos, Valoraciones_comentarios, Valoraciones_info_adicional, Valoraciones_lugar


class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('id','user_name','password','nombre','apellido','level','estado')

class LugarAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','informacion_primaria','latitud','longitud','tag','imagen','estado')

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
