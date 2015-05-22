"""APIrest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include, patterns
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from rest_framework import routers
from historynet import views
from rest_framework.urlpatterns import format_suffix_patterns

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'usuario', views.UsuarioViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^consultar_usuario/$',views.UsuarioView.as_view()),
    url(r'^consultar_usuario/(?P<username>\w+)/$',views.UsuarioView.as_view()),

    url(r'^consultar_comentarios/$',views.ComentarioView.as_view()),
    url(r'^consultar_comentarios/(?P<lugar_id>\d+)/$',views.ComentarioView.as_view()),

    url(r'^consultar_lugar/$',views.LugarView.as_view()),
    url(r'^consultar_lugar/(?P<id>\d+)/$',views.LugarView.as_view()),
    
    url(r'^consultar_lugar_cercano/(?P<lat>-?(\d+\.\d+))/(?P<log>-?(\d+\.\d+))/$',views.LugaresCercanosView.as_view()),
    

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    
]
