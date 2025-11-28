from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),

    # Login / Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Notícias
    path('noticias/', views.listar_noticias, name='lista_noticias'),
    path('noticias/<int:id>/', views.detalhar_noticia, name='detalhe_noticia'),
    path('noticias/pesquisar/', views.pesquisar_noticias, name='pesquisar_noticias'),

    # Benefícios
    path('beneficios/', views.listar_beneficios, name='lista_beneficios'),
    path('beneficios/<int:id>/', views.detalhar_beneficio, name='detalhe_beneficio'),

    # Associados
    path('associados/', views.associados_lista, name='associados_lista'),
    path('associados/<int:id>/', views.associado_detalhe, name='associado_detalhe'),

    # Páginas estáticas
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
]
