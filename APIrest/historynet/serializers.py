from .models import Usuario, Lugar, Informacion_adicional, Comentario, Lugares_favoritos, Valoraciones_comentarios, Valoraciones_info_adicional, Valoraciones_lugar
from rest_framework import serializers



class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import django.utils.six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

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
    imagen = Base64ImageField(
        max_length=None, use_url=True,
    )
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
            'imagen',
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
            'imagen',
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
