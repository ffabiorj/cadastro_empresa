from django.core.exceptions import ValidationError


def validate_cnpj(value):
    if not value.isdigit():
        raise ValidationError("CNPJ deve conter apenas números.", "digits")
    if len(value) != 14:
        raise ValidationError("CNPJ deve ter 14 numeros.", "length")
