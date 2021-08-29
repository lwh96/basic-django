
from rest_framework import generics
from .serializers import AuthTokenSerializer, RegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.


class RegisterApiView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginApiView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
