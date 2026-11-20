from django.shortcuts import render, get_object_or_404, redirect
from .forms import PedidoForm
from .models import Pedido

# Create your views here.

def add_pedido(request):
    template_name = 'pedido/add_pedido.html'
    context = {}
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('pedido:list_pedidos')
    form = PedidoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_pedidos(request):
    template_name = 'pedido/list_pedidos.html'
    pedidos = Pedido.objects.select_related('participante', 'cupom')
    context = {
        'pedidos': pedidos
    }
    return render(request, template_name, context)

def edit_pedido(request, id_pedido):
    template_name = 'pedido/add_pedido.html'
    context = {}
    pedido = get_object_or_404(Pedido, id=id_pedido)
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedido:list_pedidos')
    form = PedidoForm(instance=pedido)
    context['form'] = form
    return render(request, template_name, context)

def delete_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id=id_pedido)
    pedido.delete()
    return redirect('pedido:list_pedidos')
