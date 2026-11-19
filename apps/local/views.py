from django.shortcuts import render, get_object_or_404, redirect
from .forms import LocalForm
from .models import Local

# Create your views here.

def add_local(request):
    template_name = 'local/add_local.html'
    context = {}
    if request.method == 'POST':
        form = LocalForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('local:list_locais')
    form = LocalForm()
    context['form'] = form
    return render(request, template_name, context)

def list_locais(request):
    template_name = 'local/list_locais.html'
    locais = Local.objects.filter()
    context = {
        'locais': locais
    }
    return render(request, template_name, context)

def edit_local(request, id_local):
    template_name = 'local/add_local.html'
    context = {}
    local = get_object_or_404(Local, id=id_local)
    if request.method == 'POST':
        form = LocalForm(request.POST, request.FILES, instance=local)
        if form.is_valid():
            form.save()
            return redirect('local:list_locais')
    form = LocalForm(instance=local)
    context['form'] = form
    return render(request, template_name, context)

def delete_local(request, id_local):
    local = Local.objects.get(id=id_local)
    local.delete()
    return redirect('local:list_locais')
