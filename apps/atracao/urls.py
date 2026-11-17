from django.urls import path
from . import views

app_name = 'atracao'

urlpatterns = [
    path('listar/', views.list_atracoes, name='list_atracoes'),
    path('adicionar/', views.add_atracao, name='add_atracao'),
    path('editar/<int:id_atracao>/', views.edit_atracao, name='edit_atracao'),
    path('excluir/<int:id_atracao>/', views.delete_atracao, name='delete_atracao'),
]
