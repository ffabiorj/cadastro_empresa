from django.test import TestCase
from django.urls import reverse


class EmpresaPostTest(TestCase):
    def setUp(self):
        self.payload = {
            "razao_social": "teste",
            "nome_fantasia": "teste",
            "cnpj": "22.222.222/2222-22",
            "email": "fabio20rj@gmail.com",
            "endereco": "nereu sampaio, 61",
            "cidade": "Rio de Janeiro",
            "estado": "MG",
            "telefone": "(21)3333-3333",
            "data_cadastro": "2020-12-10",
            "status": "A",
            "risco": "C",
            "agencia": "333-3",
            "conta": "33.333-3",
        }

    def test_method_post_redirect(self):
        url = reverse("criar_empresa")
        response = self.client.post(url, data=self.payload)
        self.assertEqual(response.status_code, 200)

    def test_method_post_status_code_200(self):
        url = reverse("criar_empresa")
        response = self.client.post(url, data=self.payload, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_method_post_form_empty(self):
        url = reverse("criar_empresa")
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
