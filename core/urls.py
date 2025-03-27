from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('ver_imagens/', views.ver_imagens, name='ver_imagens'),
    path('upload/', views.upload_imagem, name='upload_imagem'),
    path('projetos/', views.projetos, name='projetos'),
    path('adicionar_projeto/', views.adicionar_projeto, name='adicionar_projeto'),
]