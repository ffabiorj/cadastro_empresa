from core.models import Empresa
from rest_framework.viewsets import ModelViewSet

from .serializers import EmpresaSerializer


class EmpresaViewSet(ModelViewSet):
    """
    Uma simples view para visualizer, criar, atualizar e deletar uma empresa.
    """

    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
