from django.contrib import admin
from django.urls import include, path
from core.views.acessorio import AcessorioViewSet
from core.views.cor import CorViewSet
from core.views.modelo import ModeloViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet

router = DefaultRouter()

router.register(r'acessorio', AcessorioViewSet)
router.register(r'cor', CorViewSet)
router.register(r'modelo', ModeloViewSet)
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
