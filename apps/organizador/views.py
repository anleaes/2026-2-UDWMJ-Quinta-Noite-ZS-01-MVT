from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrganizadorForm
from .models import Organizador

# Create your views here.

def add_organizador(request):
    template_name = 'organizador/add_organizador.html'
    context = {}
    if request.method == 'POST':
        form = OrganizadorForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('organizador:list_organizadores')
    form = OrganizadorForm()
    context['form'] = form
    return render(request, template_name, context)

def list_organizadores(request):
    template_name = 'organizador/list_organizadores.html'
    organizadores = Organizador.objects.filter()
    context = {
        'organizadores': organizadores
    }
    return render(request, template_name, context)

def edit_organizador(request, id_organizador):
    template_name = 'organizador/add_organizador.html'
    context = {}
    organizador = get_object_or_404(Organizador, id=id_organizador)
    if request.method == 'POST':
        form = OrganizadorForm(request.POST, request.FILES, instance=organizador)
        if form.is_valid():
            form.save()
            return redirect('organizador:list_organizadores')
    form = OrganizadorForm(instance=organizador)
    context['form'] = form
    return render(request, template_name, context)

def delete_organizador(request, id_organizador):
    organizador = Organizador.objects.get(id=id_organizador)
    organizador.delete()
    return redirect('organizador:list_organizadores')
