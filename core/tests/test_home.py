from django.test import TestCase
from django.urls import reverse
from core.models import Empresa


class HomeTest(TestCase):
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
        self.response = self.client.get(reverse("home"))

    def test_get_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, "index.html")

    def test_has_content_h3(self):
        self.assertContains(self.response, "Empresas")

    def test_get_page_for_id(self):
        url = reverse("visualizar_empresa", kwargs={"pk": self.empresa.id})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_get_form_update_empty(self):
        url = reverse("atualizar_empresa", kwargs={"pk": self.empresa.id})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_get_page_not_found(self):
        url = reverse("visualizar_empresa", kwargs={"pk": 10})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
