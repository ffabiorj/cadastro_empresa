from django.test import TestCase
from core.validators import valid_cnpj
from django.core.validators import ValidationError


class ValidatorTest(TestCase):
    def test_validator_invalid(self):
        self.assertRaises(ValidationError, valid_cnpj, "teste")
