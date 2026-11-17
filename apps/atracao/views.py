from django.shortcuts import render, get_object_or_404, redirect
from .forms import AtracaoForm
from .models import Atracao

# Create your views here.

def add_atracao(request):
    template_name = 'atracao/add_atracao.html'
    context = {}
    if request.method == 'POST':
        form = AtracaoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('atracao:list_atracoes')
    form = AtracaoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_atracoes(request):
    template_name = 'atracao/list_atracoes.html'
    atracoes = Atracao.objects.filter()
    context = {
        'atracoes': atracoes
    }
    return render(request, template_name, context)

def edit_atracao(request, id_atracao):
    template_name = 'atracao/add_atracao.html'
    context = {}
    atracao = get_object_or_404(Atracao, id=id_atracao)
    if request.method == 'POST':
        form = AtracaoForm(request.POST, request.FILES, instance=atracao)
        if form.is_valid():
            form.save()
            return redirect('atracao:list_atracoes')
    form = AtracaoForm(instance=atracao)
    context['form'] = form
    return render(request, template_name, context)

def delete_atracao(request, id_atracao):
    atracao = Atracao.objects.get(id=id_atracao)
    atracao.delete()
    return redirect('atracao:list_atracoes')
