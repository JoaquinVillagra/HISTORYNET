from .models import Usuario, Lugar, Informacion_adicional, Comentario, Lugares_favoritos, Valoraciones_comentarios, Valoraciones_info_adicional, Valoraciones_lugar
from rest_framework import serializers

class LugarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lugar
        fields = (
        	'url',
        	'id',
        	'nombre',
        	'direccion',
        	'informacion_primaria',
        	'longitud',
        	'latitud',
        	'fecha',
        	'valoracion',
        	'denuncia',
        	'estado'
        	)


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = (
        	'url',
        	'id',
        	'user_name',
        	'password',
        	'email',
        	'nombre',
        	'apellido',
        	'pais',
        	'sexo',
        	'level',
        	'estado',
        	'last_login',
        	)

class Informacion_adicionalSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Informacion_adicional
		fields = (
			'id',
        	'lugar_id',
        	'mensaje',
        	'fecha',
        	'denuncia',
        	'estado',
        	)

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comentario
		fields = (
			'id',
			'user_id',
			'lugar_id',
			'mensaje',
			'fecha',
			'valoracion',
			'denuncia',
			'estado',
			)

class Lugares_favoritosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lugares_favoritos
		fields = (
			'id',
			'user_id',
			'lugar_id',
			)

class Valoraciones_comentariosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Valoraciones_lugar
		fields = (
			'id',
			'comentario_id',
			'valoracion',
			)

class Valoraciones_info_adicionalSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Valoraciones_info_adicional
		fields = (
			'id',
			'user_id',
			'info_adicional_id',
			'valoracion',
			)

class Valoraciones_lugarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Valoraciones_lugar
		fields = (
			'id',
			'user_id',
			'lugar_id',
			'valoracion',
			)
