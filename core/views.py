from django.shortcuts import render
from core.models import Empresa


def home(request):
    empresas = Empresa.objects.all()
    return render(request, "index.html", {"empresas": empresas})
