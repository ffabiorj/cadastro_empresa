from django.test import TestCase
from core.validators import valid_cnpj
from django.core.validators import ValidationError


class ValidatorTest(TestCase):
    def test_validator_none(self):
        self.assertIsNone(valid_cnpj("35379838000112"))

    def test_validator_invalid(self):
        self.assertRaises(ValidationError, valid_cnpj, "teste")

    def test_validator_invalid_caracter(self):
        self.assertRaises(ValidationError, valid_cnpj, "22*222$222/222*2-22")

    def test_validator_len_more_then_14(self):
        self.assertRaises(ValidationError, valid_cnpj, "222222222222222222")
