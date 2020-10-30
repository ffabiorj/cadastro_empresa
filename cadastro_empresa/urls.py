from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import EmpresaViewSet

router = routers.DefaultRouter()
router.register(r"empresas", EmpresaViewSet, basename="empresas")


urlpatterns = [
    path("", include("core.urls")),
    path("api/v1/", include(router.urls)),
    path("admin/", admin.site.urls),
]
