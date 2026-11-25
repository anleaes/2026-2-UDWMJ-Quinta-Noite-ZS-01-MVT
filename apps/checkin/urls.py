from django.urls import path
from . import views

app_name = 'checkin'

urlpatterns = [
    path('listar/', views.list_checkins, name='list_checkins'),
    path('adicionar/', views.add_checkin, name='add_checkin'),
    path('editar/<int:id_checkin>/', views.edit_checkin, name='edit_checkin'),
    path('excluir/<int:id_checkin>/', views.delete_checkin, name='delete_checkin'),
]
