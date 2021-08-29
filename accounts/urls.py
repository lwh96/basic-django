from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('account', views.AccountViewSet)

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('', include(router.urls)),
]
