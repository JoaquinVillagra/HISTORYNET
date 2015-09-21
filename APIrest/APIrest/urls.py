from django.conf.urls import url, include, patterns
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from rest_framework import routers
from historynet import views
from rest_framework.urlpatterns import format_suffix_patterns
router = routers.DefaultRouter()

#Se define el formato de las URLs a ser usados por el protocolo HTTP en Android.



#URL_PATH = "http://46.101.184.198:8000/"
#JSON_PATH = "?format=json"

#CONSULTAR TODOS LOS USUARIOS
#url = URL_PATH + "consultar_usuario/" + JSON_PATH

#CONSULTAR POR UN USUARIO EN ESPECIFICO CON EL USERNAME
#cambiar USERNAME por el user name a consultar
#url = URL_PATH + "consultar_usuario/USERNAME/" + JSON_PATH

#CONSULTAR POR TODOS LOS COMENTARIOS REALIZADOS
#url = URL_PATH + "consultar_comentarios/" + JSON_PATH

#CONSULTAR POR LOS COMENTARIOS DE UN SOLO LUGAR
#cambiar LUGAR_ID por la id designada del lugar
#url = URL_PATH + "consultar_comentarios/LUGAR_ID/" + JSON_PATH

#CONSULTAR POR TODOS LOS LUGARES
#url = URL_PATH + "consultar_lugar/" + JSON_PATH

#CONSULTAR POR UN LUGAR EN ESPECIFICO CON EL LUGAR_ID
#cambiar LUGAR_ID por la id designada del lugar
#url = URL_PATH + "consultar_lugar/LUGAR_ID/" + JSON_PATH

#CONSULTAR POR LOS LUGARES CERCANOS A CIERTA DISTANCIA DADA UNA
#UBICACION EN LATITUD Y LONGITUD
#cambiar LATITUD, LONGITUD, KILOMETROS_A_LA_REDONDA por los datos reales.
#url = URL_PATH + "consultar_lugar_cercano/LATITUD/LONGITUD/METROS_A_LA_REDONDA/" + JSON_PATH

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^consultar_usuario/$',views.UsuarioView.as_view()),
    url(r'^consultar_usuario/(?P<username>\w+)/$',views.UsuarioView.as_view()),

    url(r'^consultar_comentarios/$',views.ComentarioView.as_view()),
    url(r'^consultar_comentarios/(?P<lugar_id>\d+)/$',views.ComentarioView.as_view()),

    url(r'^consultar_lugar/$',views.LugarView.as_view()),
    url(r'^consultar_lugar/(?P<id>\d+)/$',views.LugarView.as_view()),
    
    url(r'^consultar_lugar_cercano/(?P<lat>-?(\d+\.\d+))/(?P<log>-?(\d+\.\d+))/(?P<dist>\d+)/$',views.LugaresCercanosView.as_view()),
    

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^agregar_lugar/$',views.LugarViewAgregar.as_view()),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})

]
