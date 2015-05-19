from .models import Usuario, Lugar, Informacion_adicional
from rest_framework import viewsets
from .serializers import LoginSerializer, UsuarioSerializer, Informacion_adicionalSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class Informacion_adicionalViewSet(viewsets.ModelViewSet):
	queryset = Informacion_adicional.objects.all()
	serializer_class = Informacion_adicionalSerializer