from django.shortcuts import render, get_object_or_404, redirect
from .forms import IngressoForm
from .models import Ingresso

# Create your views here.

def add_ingresso(request):
    template_name = 'ingresso/add_ingresso.html'
    context = {}
    if request.method == 'POST':
        form = IngressoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('ingresso:list_ingressos')
    form = IngressoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_ingressos(request):
    template_name = 'ingresso/list_ingressos.html'
    ingressos = Ingresso.objects.filter()
    context = {
        'ingressos': ingressos
    }
    return render(request, template_name, context)

def edit_ingresso(request, id_ingresso):
    template_name = 'ingresso/add_ingresso.html'
    context = {}
    ingresso = get_object_or_404(Ingresso, id=id_ingresso)
    if request.method == 'POST':
        form = IngressoForm(request.POST, request.FILES, instance=ingresso)
        if form.is_valid():
            form.save()
            return redirect('ingresso:list_ingressos')
    form = IngressoForm(instance=ingresso)
    context['form'] = form
    return render(request, template_name, context)

def delete_ingresso(request, id_ingresso):
    ingresso = Ingresso.objects.get(id=id_ingresso)
    ingresso.delete()
    return redirect('ingresso:list_ingressos')
