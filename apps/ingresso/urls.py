from django.urls import path
from . import views

app_name = 'ingresso'

urlpatterns = [
    path('listar/', views.list_ingressos, name='list_ingressos'),
    path('adicionar/', views.add_ingresso, name='add_ingresso'),
    path('editar/<int:id_ingresso>/', views.edit_ingresso, name='edit_ingresso'),
    path('excluir/<int:id_ingresso>/', views.delete_ingresso, name='delete_ingresso'),
]
