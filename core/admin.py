from django.contrib import admin
from .models import (
    Beneficio,
    Associado,
    Autor,
    Endereco,
    Categoria,
    Telefone,
    Email,
    TipoBeneficio,
    GestorBeneficio,
    Noticia
)

# MODELOS SIMPLES
admin.site.register(Autor)
admin.site.register(Endereco)
admin.site.register(Categoria)
admin.site.register(Telefone)
admin.site.register(Email)
admin.site.register(TipoBeneficio)
admin.site.register(GestorBeneficio)


# BENEFÍCIO
@admin.register(Beneficio)
class BeneficioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'data_inicio', 'data_fim', 'valor_total')
    search_fields = ('nome', 'descricao')
    list_filter = ('ativo',)


# ASSOCIADO
@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'data_nascimento', 'fk_beneficio')
    search_fields = ('nome_completo', 'cpf')
    list_filter = ('fk_beneficio',)


# NOTÍCIA
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fk_autor', 'fk_categoria', 'data_publicacao', 'destaque')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('destaque', 'fk_categoria')
