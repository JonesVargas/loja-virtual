from django.contrib import admin
from .models import Produto, Banner, SecaoHome


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'promocao', 'ativo', 'criado_em')
    list_filter = ('promocao', 'ativo', 'criado_em')
    search_fields = ('nome', 'descricao')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo', 'ordem')
    list_filter = ('ativo',)
    search_fields = ('titulo', 'subtitulo')
    ordering = ('ordem',)


@admin.register(SecaoHome)
class SecaoHomeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'ordem', 'ativa', 'criado_em')
    list_filter = ('tipo', 'ativa')
    search_fields = ('nome', 'titulo', 'subtitulo', 'texto')
    filter_horizontal = ('produtos',)
    ordering = ('ordem', 'id')