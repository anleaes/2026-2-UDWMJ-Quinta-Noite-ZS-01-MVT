from django.shortcuts import render, get_object_or_404, redirect
from .forms import ParticipanteForm
from .models import Participante

# Create your views here.

def add_participante(request):
    template_name = 'participante/add_participante.html'
    context = {}
    if request.method == 'POST':
        form = ParticipanteForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('participante:list_participantes')
    form = ParticipanteForm()
    context['form'] = form
    return render(request, template_name, context)

def list_participantes(request):
    template_name = 'participante/list_participantes.html'
    participantes = Participante.objects.filter()
    context = {
        'participantes': participantes
    }
    return render(request, template_name, context)

def edit_participante(request, id_participante):
    template_name = 'participante/add_participante.html'
    context = {}
    participante = get_object_or_404(Participante, id=id_participante)
    if request.method == 'POST':
        form = ParticipanteForm(request.POST, request.FILES, instance=participante)
        if form.is_valid():
            form.save()
            return redirect('participante:list_participantes')
    form = ParticipanteForm(instance=participante)
    context['form'] = form
    return render(request, template_name, context)

def delete_participante(request, id_participante):
    participante = Participante.objects.get(id=id_participante)
    participante.delete()
    return redirect('participante:list_participantes')
