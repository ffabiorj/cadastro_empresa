from django.test import TestCase
from core.models import Empresa
from django.urls import reverse


class EmpresaUpdateTest(TestCase):
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
        self.payload = {
            "razao_social": "fabio",
            "nome_fantasia": "fabio",
            "cnpj": "22.222.222/2222-22",
            "email": "fabio20rj@gmail.com",
            "endereco": "São Joao",
            "cidade": "Minas",
            "estado": "MG",
            "telefone": "(21)3333-3333",
            "data_cadastro": "2020-12-10",
            "status": "A",
            "risco": "C",
            "agencia": "333-3",
            "conta": "33.333-3",
        }

    def test_method_update_status_code_200(self):
        url = reverse("atualizar_empresa", kwargs={"pk": self.empresa.id})
        response = self.client.post(url, data=self.payload, fallow=True)
        self.assertEqual(200, response.status_code)

    def test_method_update_wrong_id(self):
        url = reverse("atualizar_empresa", kwargs={"pk": 10})
        response = self.client.post(url, data=self.payload)
        self.assertEqual(404, response.status_code)
