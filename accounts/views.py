
from rest_framework import viewsets, generics
from .serializers import AccountSerializer, AuthTokenSerializer, RegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Account
from rest_framework.settings import api_settings
# Create your views here.


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RegisterApiView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
