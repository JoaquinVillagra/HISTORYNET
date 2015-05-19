from .models import Usuario, Lugar, Informacion_adicional
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

