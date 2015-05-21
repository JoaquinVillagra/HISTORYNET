from django.conf.urls import patterns, include, url

urlpatterns = patterns('APIrest.historynet.views',
	url(r'^consultar_lugares_cercanos/$','testview')

)