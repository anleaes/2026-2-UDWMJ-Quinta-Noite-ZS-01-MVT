from django.urls import path
from . import views

app_name = 'evento'

urlpatterns = [
    path('listar/', views.list_eventos, name='list_eventos'),
    path('adicionar/', views.add_evento, name='add_evento'),
    path('editar/<int:id_evento>/', views.edit_evento, name='edit_evento'),
    path('excluir/<int:id_evento>/', views.delete_evento, name='delete_evento'),
]
