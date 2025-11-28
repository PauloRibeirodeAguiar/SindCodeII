from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Noticia, Beneficio, Associado

# --------------------------
# HOME
# --------------------------
@login_required(login_url='login')
def home(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')[:5]
    associados = Associado.objects.all()
    return render(request, 'home.html', {'noticias': noticias, 'associados': associados})

# --------------------------
# NOTÍCIAS
# --------------------------
@login_required(login_url='login')
def listar_noticias(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'noticias/lista.html', {'noticias': noticias})

@login_required(login_url='login')
def detalhar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})

@login_required(login_url='login')
def pesquisar_noticias(request):
    query = request.GET.get('q')
    if query:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains=query) | Q(conteudo__icontains=query)
        ).order_by('-data_publicacao')
    else:
        noticias = Noticia.objects.none()
    return render(request, 'noticias/pesquisa.html', {'noticias': noticias, 'query': query})

# --------------------------
# BENEFÍCIOS
# --------------------------
@login_required(login_url='login')
def listar_beneficios(request):
    beneficios = Beneficio.objects.all()
    return render(request, 'beneficios/lista.html', {'beneficios': beneficios})

@login_required(login_url='login')
def detalhar_beneficio(request, id):
    beneficio = get_object_or_404(Beneficio, id=id)
    return render(request, 'beneficios/detalhe.html', {'beneficio': beneficio})

# --------------------------
# ASSOCIADOS
# --------------------------
@login_required(login_url='login')
def associados_lista(request):
    associados = Associado.objects.all()
    return render(request, 'associados/lista.html', {'associados': associados})

@login_required(login_url='login')
def associado_detalhe(request, id):
    associado = get_object_or_404(Associado, id=id)
    return render(request, 'associados/detalhe.html', {'associado': associado})

# --------------------------
# LOGIN / LOGOUT
# --------------------------
def login_view(request):
    next_url = request.GET.get('next', 'home')  # redireciona para a página original

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# --------------------------
# PÁGINAS ESTÁTICAS
# --------------------------
def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')
