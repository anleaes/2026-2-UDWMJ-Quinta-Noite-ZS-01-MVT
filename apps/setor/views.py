from django.shortcuts import render, get_object_or_404, redirect
from .forms import SetorForm
from .models import Setor

# Create your views here.

def add_setor(request):
    template_name = 'setor/add_setor.html'
    context = {}
    if request.method == 'POST':
        form = SetorForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('setor:list_setores')
    form = SetorForm()
    context['form'] = form
    return render(request, template_name, context)

def list_setores(request):
    template_name = 'setor/list_setores.html'
    setores = Setor.objects.select_related('local')
    context = {
        'setores': setores
    }
    return render(request, template_name, context)

def edit_setor(request, id_setor):
    template_name = 'setor/add_setor.html'
    context = {}
    setor = get_object_or_404(Setor, id=id_setor)
    if request.method == 'POST':
        form = SetorForm(request.POST, request.FILES, instance=setor)
        if form.is_valid():
            form.save()
            return redirect('setor:list_setores')
    form = SetorForm(instance=setor)
    context['form'] = form
    return render(request, template_name, context)

def delete_setor(request, id_setor):
    setor = get_object_or_404(Setor, id=id_setor)
    setor.delete()
    return redirect('setor:list_setores')
