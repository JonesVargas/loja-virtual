from django.shortcuts import render
from .models import Produto, Banner, RedeSocial


def home(request):
    produtos = Produto.objects.filter(ativo=True)
    produtos_promocao = produtos.filter(promocao=True)

    banners = Banner.objects.filter(ativo=True).order_by('ordem')
    redes = RedeSocial.objects.filter(ativo=True).order_by('ordem')

    contexto = {
        'produtos': produtos,
        'produtos_promocao': produtos_promocao,
        'banners': banners,
        'redes': redes,
    }
    return render(request, 'home.html', contexto)