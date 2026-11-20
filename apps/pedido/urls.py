from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('listar/', views.list_pedidos, name='list_pedidos'),
    path('adicionar/', views.add_pedido, name='add_pedido'),
    path('editar/<int:id_pedido>/', views.edit_pedido, name='edit_pedido'),
    path('excluir/<int:id_pedido>/', views.delete_pedido, name='delete_pedido'),
]
