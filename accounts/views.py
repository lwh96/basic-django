
from rest_framework import viewsets, generics
from .serializers import AccountSerializer, RegisterSerializer
from rest_framework.response import Response
from .models import Account
# Create your views here.


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RegisterApiView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        result = {}
        if serializer.is_valid():
            account = serializer.save()
            print('account', account)
            result["message"] = "Account has been successfully created"
            result["email"] = account.email
            result["username"] = account.username
        else:
            result = serializer.errors
        print(result)
        return Response(result)
