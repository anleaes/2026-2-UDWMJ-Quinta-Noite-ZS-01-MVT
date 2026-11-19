from django.urls import path
from . import views

app_name = 'local'

urlpatterns = [
    path('listar/', views.list_locais, name='list_locais'),
    path('adicionar/', views.add_local, name='add_local'),
    path('editar/<int:id_local>/', views.edit_local, name='edit_local'),
    path('excluir/<int:id_local>/', views.delete_local, name='delete_local'),
]
