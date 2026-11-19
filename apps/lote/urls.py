from django.urls import path
from . import views

app_name = 'lote'

urlpatterns = [
    path('listar/', views.list_lotes, name='list_lotes'),
    path('adicionar/', views.add_lote, name='add_lote'),
    path('editar/<int:id_lote>/', views.edit_lote, name='edit_lote'),
    path('excluir/<int:id_lote>/', views.delete_lote, name='delete_lote'),
]
