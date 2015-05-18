from .models import Login, Usuario
from rest_framework import serializers

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields = ('url', 'id', 'user_name', 'password', 'email', 'level', 'estado', 'last_login')


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url', 'login', 'nombre', 'apellido', 'pais', 'sexo')

