from django.forms import ModelForm
from core.models import Empresa


class CriarEmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = "__all__"
