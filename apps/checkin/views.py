from django.shortcuts import render, get_object_or_404, redirect
from .forms import CheckInForm
from .models import CheckIn

# Create your views here.

def add_checkin(request):
    template_name = 'checkin/add_checkin.html'
    context = {}
    if request.method == 'POST':
        form = CheckInForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('checkin:list_checkins')
    form = CheckInForm()
    context['form'] = form
    return render(request, template_name, context)

def list_checkins(request):
    template_name = 'checkin/list_checkins.html'
    checkins = CheckIn.objects.select_related('ingresso')
    context = {
        'checkins': checkins
    }
    return render(request, template_name, context)

def edit_checkin(request, id_checkin):
    template_name = 'checkin/add_checkin.html'
    context = {}
    checkin = get_object_or_404(CheckIn, id=id_checkin)
    if request.method == 'POST':
        form = CheckInForm(request.POST, request.FILES, instance=checkin)
        if form.is_valid():
            form.save()
            return redirect('checkin:list_checkins')
    form = CheckInForm(instance=checkin)
    context['form'] = form
    return render(request, template_name, context)

def delete_checkin(request, id_checkin):
    checkin = get_object_or_404(CheckIn, id=id_checkin)
    checkin.delete()
    return redirect('checkin:list_checkins')
