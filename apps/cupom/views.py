from django.shortcuts import render, get_object_or_404, redirect
from .forms import CupomForm
from .models import Cupom

# Create your views here.

def add_cupom(request):
    template_name = 'cupom/add_cupom.html'
    context = {}
    if request.method == 'POST':
        form = CupomForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('cupom:list_cupons')
    form = CupomForm()
    context['form'] = form
    return render(request, template_name, context)

def list_cupons(request):
    template_name = 'cupom/list_cupons.html'
    cupons = Cupom.objects.filter()
    context = {
        'cupons': cupons
    }
    return render(request, template_name, context)

def edit_cupom(request, id_cupom):
    template_name = 'cupom/add_cupom.html'
    context = {}
    cupom = get_object_or_404(Cupom, id=id_cupom)
    if request.method == 'POST':
        form = CupomForm(request.POST, request.FILES, instance=cupom)
        if form.is_valid():
            form.save()
            return redirect('cupom:list_cupons')
    form = CupomForm(instance=cupom)
    context['form'] = form
    return render(request, template_name, context)

def delete_cupom(request, id_cupom):
    cupom = Cupom.objects.get(id=id_cupom)
    cupom.delete()
    return redirect('cupom:list_cupons')
