from .models import Usuario, Lugar, Informacion_adicional
from rest_framework import viewsets
from .serializers import UsuarioSerializer, LugarSerializer, Informacion_adicionalSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

class Informacion_adicionalViewSet(viewsets.ModelViewSet):
	queryset = Informacion_adicional.objects.all()
	serializer_class = Informacion_adicionalSerializer