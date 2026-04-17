from django.contrib import admin
from .models import Produto, Banner, RedeSocial


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'promocao', 'ativo', 'criado_em')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo', 'ordem')

@admin.register(RedeSocial)
class RedeSocialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'ordem')