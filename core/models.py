from django.db import models
from core.validators import validate_cnpj


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

    razao_social = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, validators=[validate_cnpj])
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=5)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateField()
    status = models.BooleanField(default=True)
    risco = models.CharField(max_length=2, choices=RISCOS)
    agencia = models.CharField(max_length=6)
    conta = models.CharField(max_length=10)

    def __str__(self):
        return self.nome_fantasia

    class Meta:
        ordering = ["-nome_fantasia"]
