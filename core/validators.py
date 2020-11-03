import re

from django.core.exceptions import ValidationError
from validate_docbr import CNPJ

cnpj = CNPJ()


def clean_cnpj(value):
    value = re.sub(r"[-.\/]", "", value)
    return value


def valid_cnpj(value):
    value = clean_cnpj(value)
    if not cnpj.validate(value):
        raise ValidationError("Informe um CNPJ valido.")
