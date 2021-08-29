
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import Rectangle, Diamond, Square, Triangle
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class BaseViewSet(ModelViewSet):
    queryset = None
    serializer_class = None
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RectangleViewSet(BaseViewSet):
    queryset = Rectangle.objects.all()
    serializer_class = RectangleSerializer


class SquareViewSet(BaseViewSet):
    queryset = Square.objects.all()
    serializer_class = SquareSerializer


class DiamondViewSet(BaseViewSet):
    queryset = Diamond.objects.all()
    serializer_class = DiamondSerializer


class TriangleViewSet(BaseViewSet):
    queryset = Triangle.objects.all()
    serializer_class = TriangleSerializer


class AreaViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, type, pk=None):
        queryset = None
        if type == 'rectangle':
            queryset = Rectangle.objects.all()
            serializer_class = RectangleAreaSerializer
        elif type == 'square':
            queryset = Square.objects.all()
            serializer_class = RectangleAreaSerializer
        elif type == 'diamond':
            queryset = Diamond.objects.all()
            serializer_class = DiamondAreaSerializer
        elif type == 'triangle':
            queryset = Triangle.objects.all()
            serializer_class = TriangleAreaSerializer
        obj = get_object_or_404(queryset, pk=pk)
        data = serializer_class(obj).data
        print(data)
        return Response(data)


class PerimeterViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, type, pk=None):
        queryset = None
        if type == 'rectangle':
            queryset = Rectangle.objects.all()
            serializer_class = QuadrilateralPerimeterSerializer
        elif type == 'square':
            queryset = Square.objects.all()
            serializer_class = QuadrilateralPerimeterSerializer
        elif type == 'diamond':
            queryset = Diamond.objects.all()
            serializer_class = QuadrilateralPerimeterSerializer
        elif type == 'triangle':
            queryset = Triangle.objects.all()
            serializer_class = TrianglePerimeterSerializer
        obj = get_object_or_404(queryset, pk=pk)
        data = serializer_class(obj).data
        print(data)
        return Response(data)
