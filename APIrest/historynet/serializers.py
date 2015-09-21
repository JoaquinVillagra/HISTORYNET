from .models import Usuario, Lugar, Informacion_adicional, Comentario, Lugares_favoritos, Valoraciones_comentarios, Valoraciones_info_adicional, Valoraciones_lugar
from rest_framework import serializers


import base64
import binascii
import imghdr
import uuid
import sys
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.utils import six
from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import ImageField


DEFAULT_CONTENT_TYPE = "application/octet-stream"
ALLOWED_IMAGE_TYPES = (
    "jpeg",
    "jpg",
    "png",
    "gif"
)

EMPTY_VALUES = (None, '', [], (), {})


class Base64ImageField(ImageField):
    """
    A django-rest-framework field for handling image-uploads through raw post data.
    It uses base64 for en-/decoding the contents of the file.
    """
    def to_internal_value(self, base64_data):
        # Check if this is a base64 string
        if base64_data in EMPTY_VALUES:
            return None

        if isinstance(base64_data, six.string_types):
            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(base64_data)
            except (TypeError, binascii.Error):
                raise ValidationError(_("Please upload a valid image."))
            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)
            if file_extension not in ALLOWED_IMAGE_TYPES:
                raise ValidationError(_("The type of the image couldn't been determined."))
            complete_file_name = file_name + "." + file_extension
            data = ContentFile(decoded_file, name=complete_file_name)
            return super(Base64ImageField, self).to_internal_value(data)
        raise ValidationError(_('This is not an base64 string'))

    def to_representation(self, value):
        # Return url including domain name.
        return value.name

    def get_file_extension(self, filename, decoded_file):
        extension = imghdr.what(filename, decoded_file)
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
