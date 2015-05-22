from .models import Usuario, Lugar, Informacion_adicional, Comentario, Lugares_favoritos, Valoraciones_comentarios, Valoraciones_info_adicional, Valoraciones_lugar
from rest_framework import viewsets
from .serializers import UsuarioSerializer, LugarSerializer, Informacion_adicionalSerializer, ComentarioSerializer, Lugares_favoritosSerializer, Valoraciones_comentariosSerializer, Valoraciones_info_adicionalSerializer, Valoraciones_lugarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404

#Vista donde se puede consultar por todos los usuarios o por
#un usuario en especifico con el username (login)
class UsuarioView(APIView):
    
    serializer_class = UsuarioSerializer

    def get(self,request,username=None,format=None):
        if id != None: # Si no se ingresa ID en la url
            users = get_object_or_404(Usuario,user_name=username)
            many = False
        else:
            users = list(Usuario.objects.all())
            many = True
            if not my_objects:
                raise Http404("No hay usuarios registrados.")
        response = self.serializer_class(users,many=many)
        return Response(response.data)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class Lugares_favoritosViewSet(viewsets.ModelViewSet):
    queryset = Lugares_favoritos.objects.all()
    serializer_class = Lugares_favoritosSerializer

class Valoraciones_comentariosViewSet(viewsets.ModelViewSet):
    queryset = Valoraciones_comentarios.objects.all()
    serializer_class = Valoraciones_comentariosSerializer

class Informacion_adicionalViewSet(viewsets.ModelViewSet):
	queryset = Informacion_adicional.objects.all()
	serializer_class = Informacion_adicionalSerializer

class Valoraciones_info_adicionalViewSet(viewsets.ModelViewSet):
    queryset = Valoraciones_info_adicional.objects.all()
    serializer_class = Valoraciones_info_adicionalSerializer

class Valoraciones_lugarViewSet(viewsets.ModelViewSet):
    queryset = Valoraciones_lugar.objects.all()
    serializer_class = Valoraciones_lugarSerializer
