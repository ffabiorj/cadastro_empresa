from core.forms import CriarEmpresaForm
from django.test import TestCase


class EmpresaFormTest(TestCase):
    def test_form_has_field(self):
        form = CriarEmpresaForm()
        expected = [
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
        self.assertSequenceEqual(expected, list(form.fields))

    def test_error_razao_social(self):
        form = self.make_validated_form(razacao_social=1)
        self.assertFalse(form.errors)

    def test_error_cnpj(self):
        form = self.make_validated_form(cnpj=1)
        self.assertFalse(form.errors)

    def make_validated_form(self, **kwargs):
        valid = dict(
            razao_social="teste",
            nome_fantasia="teste",
            cnpj="22.222.222/2222-22",
            email="fabio20rj@gmail.com",
            endereco="nereu sampaio, 61",
            cidade="Rio de Janeiro",
            estado="MG",
            telefone="(21)3333-3333",
            data_cadastro="2020-12-10",
            status="A",
            risco="C",
            agencia="333-3",
            conta="33.333-3",
        )
        data = dict(valid, **kwargs)
        form = CriarEmpresaForm(data)
        form.is_valid()
        return form
