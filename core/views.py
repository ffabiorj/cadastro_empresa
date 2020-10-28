from django.shortcuts import redirect, render, get_object_or_404

from core.models import Empresa

from .forms import CriarEmpresaForm


def home(request):
    empresas = Empresa.objects.all()
    return render(request, "index.html", {"empresas": empresas})


def criar_empresa(request):
    if request.method == "POST":
        form = CriarEmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CriarEmpresaForm()

    return render(request, "create.html", {"form": form})


def atualizar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == "POST":
        form = CriarEmpresaForm(data=request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CriarEmpresaForm(instance=empresa)

    return render(request, "update.html", {"form": form})
