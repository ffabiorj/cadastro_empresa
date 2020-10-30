from django.core.exceptions import ValidationError
import re


def valid_cnpj(value):
    value = re.sub(r"\D", "", value)
    if not value.isdigit():
        raise ValidationError("Informe um CNPJ valido.", "digitos")
