from django.urls import path
from . import views

app_name = 'setor'

urlpatterns = [
    path('listar/', views.list_setores, name='list_setores'),
    path('adicionar/', views.add_setor, name='add_setor'),
    path('editar/<int:id_setor>/', views.edit_setor, name='edit_setor'),
    path('excluir/<int:id_setor>/', views.delete_setor, name='delete_setor'),
]
