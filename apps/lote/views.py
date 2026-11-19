from django.shortcuts import render, get_object_or_404, redirect
from .forms import LoteForm
from .models import Lote

# Create your views here.

def add_lote(request):
    template_name = 'lote/add_lote.html'
    context = {}
    if request.method == 'POST':
        form = LoteForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('lote:list_lotes')
    form = LoteForm()
    context['form'] = form
    return render(request, template_name, context)

def list_lotes(request):
    template_name = 'lote/list_lotes.html'
    lotes = Lote.objects.filter()
    context = {
        'lotes': lotes
    }
    return render(request, template_name, context)

def edit_lote(request, id_lote):
    template_name = 'lote/add_lote.html'
    context = {}
    lote = get_object_or_404(Lote, id=id_lote)
    if request.method == 'POST':
        form = LoteForm(request.POST, request.FILES, instance=lote)
        if form.is_valid():
            form.save()
            return redirect('lote:list_lotes')
    form = LoteForm(instance=lote)
    context['form'] = form
    return render(request, template_name, context)

def delete_lote(request, id_lote):
    lote = Lote.objects.get(id=id_lote)
    lote.delete()
    return redirect('lote:list_lotes')
