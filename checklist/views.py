from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Registro

def crear_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroForm()
    return render(request, 'crear_registro.html', {'form': form})


def lista_registros(request):
    registros = Registro.objects.all()
    return render(request, 'lista_registros.html', {'registros': registros})
