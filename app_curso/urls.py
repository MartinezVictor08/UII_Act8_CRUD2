from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.ver_curso, name='ver_curso'),
    path('agregar/', views.agregar_curso, name='agregar_curso'),
    path('editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('borrar/<int:id>/', views.borrar_curso, name='borrar_curso'),
]