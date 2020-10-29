from core.models import Empresa
from django.test import TestCase


class EmpresaModelTest(TestCase):
    def setUp(self):
        self.empresa = Empresa.objects.create(
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

    def test_conta_uma_empresa(self):
        assert Empresa.objects.count() == 1

    def test_verifica_str(self):
        assert self.empresa.__str__() == "teste"
