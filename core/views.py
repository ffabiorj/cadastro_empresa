from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from core.models import Empresa

from .forms import CriarEmpresaForm


def home(request):
    empresas = Empresa.objects.all()
    return render(request, "index.html", {"empresas": empresas})


def criar_empresa(request):
    form = CriarEmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Empresa criada com sucesso.")
        return redirect("home")

    context = {"form": form}

    return render(request, "create.html", context)


def visualizar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    return render(request, "visualizar.html", {"empresa": empresa})


def atualizar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == "POST":
        form = CriarEmpresaForm(data=request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, "Empresa atualizada com sucesso.")
            return redirect("home")
    else:
        form = CriarEmpresaForm(instance=empresa)

    return render(request, "update.html", {"form": form})


def excluir_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    empresa.delete()
    messages.success(request, "Empresa excluída com sucesso.")
    return redirect("home")
