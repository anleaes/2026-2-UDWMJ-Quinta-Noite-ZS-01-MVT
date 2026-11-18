from django.urls import path
from . import views

app_name = 'organizador'

urlpatterns = [
    path('listar/', views.list_organizadores, name='list_organizadores'),
    path('adicionar/', views.add_organizador, name='add_organizador'),
    path('editar/<int:id_organizador>/', views.edit_organizador, name='edit_organizador'),
    path('excluir/<int:id_organizador>/', views.delete_organizador, name='delete_organizador'),
]
