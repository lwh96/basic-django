
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import DiamondAreaSerializer, QuadrilateralPerimeterSerializer, RectangleAreaSerializer, RectangleSerializer, DiamondSerializer, SquareSerializer, TriangleAreaSerializer, TrianglePerimeterSerializer, TriangleSerializer
from .models import Rectangle, Diamond, Square, Triangle
from rest_framework.response import Response
# Create your views here.


class RectangleViewSet(ModelViewSet):
    queryset = Rectangle.objects.all()
    serializer_class = RectangleSerializer


class SquareViewSet(ModelViewSet):
    queryset = Square.objects.all()
    serializer_class = SquareSerializer


class DiamondViewSet(ModelViewSet):
    queryset = Diamond.objects.all()
    serializer_class = DiamondSerializer


class TriangleViewSet(ModelViewSet):
    queryset = Triangle.objects.all()
    serializer_class = TriangleSerializer


class AreaViewSet(viewsets.ViewSet):
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
