from django.urls import path
from . import views

app_name = 'cupom'

urlpatterns = [
    path('listar/', views.list_cupons, name='list_cupons'),
    path('adicionar/', views.add_cupom, name='add_cupom'),
    path('editar/<int:id_cupom>/', views.edit_cupom, name='edit_cupom'),
    path('excluir/<int:id_cupom>/', views.delete_cupom, name='delete_cupom'),
]
