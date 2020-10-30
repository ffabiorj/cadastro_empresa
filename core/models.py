from django.db import models
from django.core.validators import validate_email
from core.validators import valid_cnpj

# from core.validators import valid_date


class Empresa(models.Model):
    RISCOS = [
        ("AA", "AA"),
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
        ("F", "F"),
        ("G", "G"),
        ("H", "H"),
    ]

    STATUS = [("A", "Ativo"), ("I", "Inativo")]

    ESTADO = [
        ("AC", "AC"),
        ("AL", "AL"),
        ("AP", "AP"),
        ("AM", "AM"),
        ("BA", "BA"),
        ("CE", "CE"),
        ("ES", "ES"),
        ("GO", "GO"),
        ("MA", "MA"),
        ("MT", "MT"),
        ("MS", "MS"),
        ("MG", "MG"),
        ("PA", "PA"),
        ("PB", "PB"),
        ("PR", "PR"),
        ("PE", "PE"),
        ("PI", "PI"),
        ("RJ", "RJ"),
        ("RN", "RN"),
        ("RS", "RS"),
        ("RO", "RO"),
        ("RR", "RR"),
        ("SC", "SC"),
        ("SP", "SP"),
        ("SE", "SE"),
        ("TO", "TO"),
        ("DF", "DF"),
    ]

    razao_social = models.CharField(max_length=200, blank=False)
    nome_fantasia = models.CharField(max_length=200, blank=True)
    cnpj = models.CharField(max_length=19, blank=False, validators=[valid_cnpj])
    email = models.EmailField(blank=True, validators=[validate_email])
    endereco = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=20, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADO, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    data_cadastro = models.DateField()
    status = models.CharField(max_length=6, choices=STATUS, blank=True)
    risco = models.CharField(max_length=2, choices=RISCOS, blank=True)
    agencia = models.CharField(max_length=6, blank=True)
    conta = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.nome_fantasia

    class Meta:
        ordering = ["-nome_fantasia"]
