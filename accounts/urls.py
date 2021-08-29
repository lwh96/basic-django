from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('account', views.AccountViewSet)

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('login/', views.LoginApiView.as_view(), name='auth'),
    path('', include(router.urls)),
]
