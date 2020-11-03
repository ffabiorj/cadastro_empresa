from django.forms import ModelForm
from core.models import Empresa


class CriarEmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = [
            "razao_social",
            "nome_fantasia",
            "cnpj",
            "email",
            "endereco",
            "cidade",
            "estado",
            "telefone",
            "data_cadastro",
            "status",
            "risco",
            "agencia",
            "conta",
        ]
