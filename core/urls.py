from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('rectangle', views.RectangleViewSet)
router.register('square', views.SquareViewSet)
router.register('diamond', views.DiamondViewSet)
router.register('triangle', views.TriangleViewSet)

urlpatterns = [
    path('area/<str:type>/<int:pk>/',
         views.AreaViewSet.as_view({'get': 'retrieve'})),
    path('perimeter/<str:type>/<int:pk>/',
         views.PerimeterViewSet.as_view({'get': 'retrieve'})),
    path('', include(router.urls)),
]
