from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Produto, Banner, RedeSocial


def home(request):
    criar_admin()
    
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

def criar_admin():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='JonesVargas',
            email='jonesvargas10980@gmail.com',
            password='@Mor1311'
        )