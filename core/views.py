from django.shortcuts import render, get_object_or_404
from .models import Noticia
from django.shortcuts import render
from .models import Beneficio
from django.db.models import Q

def pesquisar_noticias(request):
    query = request.GET.get('q')
    if query:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains=query) | Q(conteudo__icontains=query)
        ).order_by('-data_publicacao')
    else:
        noticias = Noticia.objects.none()
    return render(request, 'noticias/pesquisa.html', {'noticias': noticias, 'query': query})


def listar_beneficios(request):
    beneficios = Beneficio.objects.all()
    return render(request, 'beneficios/lista.html', {'beneficios': beneficios})

def detalhar_beneficio(request, id):
    beneficio = get_object_or_404(Beneficio, id=id)
    return render(request, 'beneficios/detalhe.html', {'beneficio': beneficio})


def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')


def home(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')[:5]
    return render(request, 'home.html', {'noticias': noticias})


def listar_noticias(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'noticias/lista.html', {'noticias': noticias})


def detalhar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})
