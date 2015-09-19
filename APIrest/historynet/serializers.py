from .models import Usuario, Lugar, Informacion_adicional, Comentario, Lugares_favoritos, Valoraciones_comentarios, Valoraciones_info_adicional, Valoraciones_lugar
from rest_framework import serializers



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
        	'id',
        	'user_name',
        	'password',
        	'email',
        	'nombre',
        	'apellido',
        	'pais',
            'ciudad',
        	'sexo',
        	'level',
        	'estado',
        	)
        read_only_fields = ('level','estado')

class Usuario2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
        	'id',
        	'nombre',
        	'apellido',
        	)

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = (
        	'id',
        	'nombre',
        	'direccion',
        	'informacion_primaria',
        	'latitud',
            'longitud',
            'tag',
        	'fecha',
            'cant_valoracion',
        	'prom_valoracion',
        	'denuncia',
        	'estado'
        	)
        read_only_fields = (
            'fecha',
            'cant_valoracion',
            'prom_valoracion',
            'denuncia',
            'estado'
            )
    def create(validated_data):
            nombre = validated_data.get('nombre', None)
            direccion = validated_data.get('direccion', None)
            informacion_primaria = validated_data.get('informacion_primaria', None)
            latitud = validated_data.get('latitud', None)
            longitud = validated_data.get('longitud', None)
            tag = validated_data.get('tag', None)
            return Lugar.objects.create(nombre=nombre,direccion=direccion,informacion_primaria=informacion_primaria,latitud=latitud,longitud=longitud,tag=tag)


class LugarDistanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = (
        	'id',
        	'nombre',
        	'direccion',
        	'informacion_primaria',
        	'longitud',
        	'latitud',
            'tag',
        	'fecha',
            'cant_valoracion',
        	'prom_valoracion',
        	'denuncia',
        	'estado',
        	'a_distancia_b'
        	)

class Lugar2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = (
        	'id',
        	'nombre',
        	)

class Informacion_adicionalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Informacion_adicional
		fields = (
			'id',
        	'lugar_id',
        	'mensaje',
            'fecha',
        	'cant_valoracion',
            'prom_valoracion',
            'denuncia',
        	'estado',
        	)
        read_only_fields = (
            'fecha',
            'cant_valoracion',
            'prom_valoracion',
            'denuncia',
            'estado'
            )

class ComentarioSerializer(serializers.ModelSerializer):
	
	lugar_id = Lugar2Serializer(many=False,read_only=True)
	user_id = Usuario2Serializer(many=False,read_only=True)
	class Meta:
		model = Comentario
		fields = (
			'id',
			'user_id',
			'lugar_id',
			'mensaje',
			'fecha',
			'cant_valoracion',
            'prom_valoracion',
            'denuncia',
			'estado',
			)
        read_only_fields = (
            'fecha',
            'cant_valoracion',
            'prom_valoracion',
            'denuncia',
            'estado'
            )

class Lugares_favoritosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lugares_favoritos
		fields = (
			'id',
			'user_id',
			'lugar_id',
			)

class Valoraciones_comentariosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Valoraciones_lugar
		fields = (
			'id',
            'user_id',
			'comentario_id',
			'valoracion',
			)

class Valoraciones_info_adicionalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Valoraciones_info_adicional
		fields = (
			'id',
			'user_id',
			'info_adicional_id',
			'valoracion',
			)

class Valoraciones_lugarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Valoraciones_lugar
		fields = (
			'id',
			'user_id',
			'lugar_id',
			'valoracion',
			)
