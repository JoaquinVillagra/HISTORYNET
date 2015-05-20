from django.contrib import admin
from .models import Usuario, Lugar, Informacion_adicional, Comentario, Lugares_favoritos, Valoraciones_comentarios, Valoraciones_info_adicional, Valoraciones_lugar

class LugarAdmin(admin.ModelAdmin):
	list_display = ('nombre','informacion_primaria','imagen_lugar')

	def imagen_lugar(self, lugar):
		url = lugar.url_imagen()
		tag = "<img src='%s' >" % url
		return tag

	imagen_lugar.allow_tags = True


admin.site.register(Usuario)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Informacion_adicional)
admin.site.register(Comentario)
admin.site.register(Lugares_favoritos)
admin.site.register(Valoraciones_comentarios)
admin.site.register(Valoraciones_lugar)
admin.site.register(Valoraciones_info_adicional)
