from django.contrib.auth.models import Login, Usuario
from rest_framework import viewsets
from APIrest.historynet.serializers import LoginSerializer, UsuarioSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer