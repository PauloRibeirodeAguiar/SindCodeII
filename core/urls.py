from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noticias/', views.listar_noticias, name='lista_noticias'),
    path('noticias/<int:id>/', views.detalhar_noticia, name='detalhe_noticia'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('beneficios/', views.listar_beneficios, name='lista_beneficios'),
    path('beneficios/<int:id>/', views.detalhar_beneficio, name='detalhe_beneficio'),
    path('noticias/pesquisar/', views.pesquisar_noticias, name='pesquisar_noticias'),

]
