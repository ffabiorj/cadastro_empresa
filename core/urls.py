from django.urls import path
from core.views import (
    home,
    criar_empresa,
    atualizar_empresa,
    excluir_empresa,
    visualizar_empresa,
)

urlpatterns = [
    path("", home, name="home"),
    path("criar/", criar_empresa, name="criar_empresa"),
    path("vizualizar/<int:pk>", visualizar_empresa, name="visualizar_empresa"),
    path("editar/<int:pk>", atualizar_empresa, name="atualizar_empresa"),
    path("excluir/<int:pk>", excluir_empresa, name="excluir_empresa"),
]
