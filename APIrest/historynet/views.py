from .models import Usuario, Lugar, Informacion_adicional, Comentario, Lugares_favoritos, Valoraciones_comentarios, Valoraciones_info_adicional, Valoraciones_lugar
from rest_framework import viewsets
from .serializers import UsuarioSerializer, LugarSerializer, Informacion_adicionalSerializer, ComentarioSerializer, Lugares_favoritosSerializer, Valoraciones_comentariosSerializer, Valoraciones_info_adicionalSerializer, Valoraciones_lugarSerializer, LugarDistanciaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404
from .coordenada import haversine

#VERBOS

#GET (Obtener 1 o mas objetos)
#POST (Crear 1 o mas objetos)
#PUT, PATCH (modificar objetos)
#DELETE (borrar 1 o mas objetos)

views.py

Una "views" o vistas es simplemente una función en Python que toma un una petición web y responde con una respuesta web.
Las respuesta será en muchos formatos, pero el que se usará en la aplicación será JSON.
Django Rest Framework proporciona una clase que heredan las funciones llamada "APIView", que además de procesar los "request/response", provee de una interfaz
donde se puede realizar consultas a la API generada.


#Vista donde se puede consultar por todos los usuarios o por
#un usuario en especifico con el username (login) y retorna todos los datos.
#http://46.101.184.198:8000/consultar_usuario/?format=json
#http://46.101.184.198:8000/consultar_usuario/USERNAME/?format=json
class UsuarioView(APIView):
    
    serializer_class = UsuarioSerializer

    def get(self,request,username=None,format=None):
        if username != None: # Si no se ingresa ID en la url
            users = get_object_or_404(Usuario,user_name=username)
            many = False
        else:
            users = Usuario.objects.all()
            many = True
        response = self.serializer_class(users,many=many)
        return Response(response.data)

    # Deshabilitado hasta que lo haga funcionar :c
    #def post(self,request,format=None):

        #new_user = self.serializer_class(data=request.DATA)
        #if new_user.is_valid():
            #obj = new_user.object
            #obj.save()
            #resp = self.serializer_class(obj,many=False)
            #return Response(resp.data)
        #else:
            #return Response(new_user.errors)


#Vista donde se pueden consultar todos los lugares o 
#consultar un lugar especifico dado la id del lugar
# http://46.101.184.198:8000/consultar_lugar/?format=json
# http://46.101.184.198:8000/consultar_lugar/ID_LUGAR?format=json
class LugarView(APIView):

    serializer_class = LugarSerializer

    def get(self,request,id=None,format=None):
        if id != None:
            lugares = get_object_or_404(Lugar,pk=id)
            many = False
        else:
            lugares = Lugar.objects.all()
            many = True
        response = self.serializer_class(lugares,many=many)
        return Response(response.data)



#Consulta de lugares cercanos
#http://46.101.184.198:8000/consultar_lugar_cercano/LATITUD/LONGITUD/DISTANCIA?format=json
#Ejem: http://46.101.184.198:8000/consultar_lugar_cercano/-33.83713/-70.73925/200/?format=json
class LugaresCercanosView(APIView):

    serializer_class = LugarDistanciaSerializer

    def get(self,request,lat=None,log=None,dist=None,format=None):
        if lat != None and log != None and dist != None:
            lugares = Lugar.objects.all()
            lugares_dist = []
            for lugar in lugares:
                a = haversine(float(log),float(lat),float(lugar.longitud),float(lugar.latitud))
                Lugar.objects.filter(pk=lugar.pk).update(a_distancia_b=a)
            lugares_2 = Lugar.objects.all()
            for lugar in lugares_2:
                if float(lugar.a_distancia_b) <= float(dist):
                    lugares_dist.append(lugar)
            response = self.serializer_class(lugares_dist,many=True)
            return Response(response.data)
        else:
            raise Http404("Error")



#Vista donde se consulta por todos los comentarios o por
#los comentarios especificos de un lugar.
#http://46.101.184.198:8000/consultar_comentarios/?format=json
#http://46.101.184.198:8000/consultar_lugar_cercano/ID_LUGAR/?format=json
class ComentarioView(APIView):

    serializer_class = ComentarioSerializer

    def get(self,request,lugar_id=None,format=None):
        if lugar_id != None:
            comentarios = get_list_or_404(Comentario,lugar_id=lugar_id)
        else:
            comentarios = Comentario.objects.all()
        response = self.serializer_class(comentarios,many=True)
        return Response(response.data)

